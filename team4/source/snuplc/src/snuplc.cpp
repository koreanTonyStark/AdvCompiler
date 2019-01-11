//------------------------------------------------------------------------------
/// @brief SnuPL compiler
/// @author Bernhard Egger <bernhard@csap.snu.ac.kr>
/// @section changelog Change Log
/// 2012/09/14 Bernhard Egger created
/// 2013/06/06 Bernhard Egger adapted to new IR/backend for SnuPL/0
/// 2014/11/30 Bernhard Egger proper argument handling
///
/// @section license_section License
/// Copyright (c) 2012-2018, Computer Systems and Platforms Laboratory, SNU
/// All rights reserved.
///
/// Redistribution and use in source and binary forms,  with or without modifi-
/// cation, are permitted provided that the following conditions are met:
///
/// - Redistributions of source code must retain the above copyright notice,
///   this list of conditions and the following disclaimer.
/// - Redistributions in binary form must reproduce the above copyright notice,
///   this list of conditions and the following disclaimer in the documentation
///   and/or other materials provided with the distribution.
///
/// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
/// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,  BUT NOT LIMITED TO,  THE
/// IMPLIED WARRANTIES OF MERCHANTABILITY  AND FITNESS FOR A PARTICULAR PURPOSE
/// ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT HOLDER  OR CONTRIBUTORS BE
/// LIABLE FOR ANY DIRECT,  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSE-
/// QUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF  SUBSTITUTE
/// GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
/// HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN  CONTRACT, STRICT
/// LIABILITY, OR TORT  (INCLUDING NEGLIGENCE OR OTHERWISE)  ARISING IN ANY WAY
/// OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
/// DAMAGE.
//------------------------------------------------------------------------------

#include <cassert>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

#include "scanner.h"
#include "parser.h"
#include "ir.h"
#include "backend.h"
#include "cfg.h"
#include "constant_propagation.h"
#include "deadcode_elimination.h"

using namespace std;

enum OPT {
	NoOpt=0,
	DeadOpt,
	ConstOpt,
	FinOpt,
};

bool dump_ast = false;
bool dump_tac = false;
bool dump_cfg = false;
bool dump_asm = true;
bool dump_dot = true;
bool run_dot = true;
bool run_gcc = false;
bool do_const = false;
bool do_dead = false;

string rte_path = "rte/IA32/";
//string rte_path = "test/rte/IA32/";
//string rte_path = "source/test/rte/IA32/";

vector<string> files;

void Syntax(string msg) {
	if (msg != "")
		cout << msg << endl << endl;

	cout << "Usage: snuplc [OPTIONS] FILES..." << endl
			<< "Compile each source file in FILES using OPTIONS." << endl
			<< "Example: snuplc fibonacci.mod" << endl << endl
			<< "Options:" << endl
			<< "  --ast          output the AST in textual/graphical form. Default: off" << endl
			<< "  --tac          output the IR in textual/graphical form. Default: off" << endl
			<< "  --cfg          output the CFG in graphical form. Default: off" << endl
			<< "  --const        do constant propagation. Default: off" << endl
			<< "  --dead         do dead code elimination. Default: off" << endl
			<< "  --exe          generate executable from compiled assembly file. Default: off" << endl
			<< "  --no-asm       output assembly code to console instead of a file. Default: file" << endl
			<< "  --no-dot       do not output the AST/IR/CFG in graphical form. Default: output in graphical form" << endl
			<< "  --no-run-dot   do not run the dot command automatically. Default: run automatically" << endl << endl << endl
			<< "Examples:" << endl
			<< "  compile fibonacci.mod and write generated assembly code to fibonacci.mod.s" << endl
			<< "  $ snuplc fibonacci.mod" << endl << endl
			<< "  compile fibonacci.mod to fibonacci.mod.s, then generate fibonacci executable" << endl
			<< "  $ snuplc --exe fibonacci.mod" << endl << endl
			<< "  compile fibonacci.mod and also output the AST in textual and graphical form" << endl
			<< "  The AST is saved in fibonacci.mod.ast (textual) and fibonacci.mod.ast.dot (graphical form)" << endl
			<< "  $ snuplc --ast fibonacci.mod" << endl << endl
			<< "  compile fibonacci.mod and also output the IR in textual and graphical form" << endl
			<< "  The IR is saved in fibonacci.mod.tac (textual) and fibonacci.mod.tac.dot (graphical form)" << endl
			<< "  $ snuplc --tac fibonacci.mod" << endl << endl;

	exit(EXIT_FAILURE);
}

void ParseArgs(int argc, char *argv[]) {
	int i = 1;

	while (i < argc) {
		if ((strlen(argv[i]) >= 2) && (argv[i][0] == '-') && (argv[i][1] == '-')) {
			if (strcmp(argv[i], "--ast") == 0)
				dump_ast = true;
			else if (strcmp(argv[i], "--tac") == 0)
				dump_tac = true;
			else if (strcmp(argv[i], "--cfg") == 0)
				dump_cfg = true;
			else if (strcmp(argv[i], "--no-asm") == 0)
				dump_asm = false;
			else if (strcmp(argv[i], "--no-dot") == 0)
				dump_dot = false;
			else if (strcmp(argv[i], "--no-run-dot") == 0)
				run_dot = false;
			else if (strcmp(argv[i], "--const") == 0)
				do_const = true;
			else if (strcmp(argv[i], "--dead") == 0)
				do_dead = true;
			else if (strcmp(argv[i], "--exe") == 0)
				run_gcc = true;
			else if (strcmp(argv[i], "--rte") == 0) {
				i++;
				if (i == argc)
					Syntax("Missing argument after --rte");
				rte_path = string(argv[i]);
			}
			else if (strcmp(argv[i], "--help") == 0)
				Syntax("");
			else
				Syntax("Unknown command line option '" + string(argv[i]) + "'.");
		} else
			files.push_back(string(argv[i]));
		i++;
	}
}

void RunDOT(string file) {
	if (run_dot) {
		ostringstream cmd;
		cmd << "dot -Tpdf -o" << file << ".pdf " << file;

		cout << "  running command '" << cmd.str() << "'..." << endl;
		if (system(cmd.str().c_str()) < 0) {
			cout << "  failed to run dot." << endl;
		}
	}
}

void RunCompile(string file, OPT opt) {
	if (run_gcc) {
		ostringstream cmd;

		string exe(file);
		exe.erase(exe.find(".mod"));

		switch (opt){
		case DeadOpt: exe += ".dead"; break;
		case ConstOpt: exe += ".const"; break;
		case FinOpt: exe += ".const.dead"; break;
		}

		cmd << "gcc -m32 -o" << exe << " " << rte_path << "IO.s" << " "
				<< rte_path << "ARRAY.s" << " " << file;

		cout << "  running command '" << cmd.str() << "'..." << endl;
		if (system(cmd.str().c_str()) < 0) {
			cout << "  failed to run gcc." << endl;
		}
	}
}

void DumpASM(string file, CModule *m, OPT opt){
	// output x86 assembly to console or file
	ostream *out = &cout;
	ofstream *sout = NULL;

	if (dump_asm) {
		sout = new ofstream(file + ".s");
		out = sout;
	}

	CBackend *be = new CBackendx86(*out);
	be->Emit(m);

	if (sout != NULL) {
		sout->flush();
		delete sout;
	}

	RunCompile(file + ".s", opt);

	delete be;
}

void DumpAST(string file, CAstModule *ast) {
	if (dump_ast) {
		assert(ast != NULL);

		// output AST in textual form
		ofstream out(file + ".ast");
		out << file << ":" << endl;
		ast->print(out, 4);
		out << endl << endl << "  symbol table:" << endl;
		ast->GetSymbolTable()->print(out, 4);
		out << endl;

		// output AST in graphical form
		if (dump_dot) {
			string fn = file + ".ast.dot";
			ofstream dot(fn);
			dot << "digraph AST {" << endl
					<< "  graph [fontname=\"Times New Roman\",fontsize=10];"
					<< endl << "  node  [fontname=\"Courier New\",fontsize=10];"
					<< endl
					<< "  edge  [fontname=\"Times New Roman\",fontsize=10];"
					<< endl << endl;
			ast->toDot(dot, 2);
			dot << "}" << endl;
			dot.flush();

			RunDOT(fn);
		}
	}
}

void DumpTAC(string file, CModule *m) {
	if (dump_tac) {
		assert(m != NULL);

		// output TAC in textual form
		ofstream out(file + ".tac");
		out << file << ":" << endl << m << endl;

		// output TAC in graphical form
		if (dump_dot) {
			string fn = file + ".tac.dot";

			ofstream dot(fn);

			dot << "digraph IR {" << endl
					<< "  graph [fontname=\"Times New Roman\",fontsize=10];"
					<< endl << "  node  [fontname=\"Courier New\",fontsize=10];"
					<< endl
					<< "  edge  [fontname=\"Times New Roman\",fontsize=10];"
					<< endl << endl;
			m->toDot(dot, 2);
			const vector<CScope*> &proc = m->GetSubscopes();
			for (size_t p = 0; p < proc.size(); p++) {
				proc[p]->toDot(dot, 2);
			}
			dot << "}" << endl;
			dot.flush();

			RunDOT(fn);
		}
	}
}

void DumpCfgIntraProc(string file, CfgIntraProc *cfg) {
	if (dump_cfg) {
		assert(cfg != NULL);
		// output CFG in graphical form
		if (dump_dot) {
			string fn = file + ".cfg.intra.dot";

			ofstream dot(fn);

			dot << "digraph CFG {" << endl
					<< "  graph [fontname=\"Times New Roman\",fontsize=10];"
					<< endl << "  node  [fontname=\"Courier New\",fontsize=10];"
					<< endl
					<< "  edge  [fontname=\"Times New Roman\",fontsize=10];"
					<< endl;
			cfg->toDot(dot);
			dot << "}" << endl;
			dot.flush();

			RunDOT(fn);
		}
	}
}

void DumpCfgInterProc(string file, CfgInterProc *cfg) {
	if (dump_cfg) {
		assert(cfg != NULL);
		// output CFG in graphical form
		if (dump_dot) {
			string fn = file + ".cfg.inter.dot";

			ofstream dot(fn);

			dot << "digraph CfgInterProc {" << endl
					<< "  graph [fontname=\"Times New Roman\",fontsize=10];"
					<< endl << "  node  [fontname=\"Courier New\",fontsize=10];"
					<< endl
					<< "  edge  [fontname=\"Times New Roman\",fontsize=10];"
					<< endl;
			cfg->toDot(dot);
			dot << "}" << endl;
			dot.flush();

			RunDOT(fn);
		}
	}
}

int main(int argc, char *argv[]) {
	ParseArgs(argc, argv);

	vector<string>::const_iterator it = files.begin();

	if (it == files.end())
		Syntax("No input files.");

	while (it != files.end()) {
		string file = *it++;

		// scanning, parsing & semantical analysis
		CScanner *s = new CScanner(new ifstream(file));
		CParser *p = new CParser(s);

		cout << "compiling " << file << "..." << endl;
		CAstNode *ast = p->Parse();

		if (p->HasError()) {
			const CToken *error = p->GetErrorToken();
			cout << "parse error at " << error->GetLineNumber() << ":"
					<< error->GetCharPosition() << " : " << p->GetErrorMessage()
					<< endl;
		}
		else {
			DumpAST(file, dynamic_cast<CAstModule*>(ast));

			// AST to TAC conversion
			CModule *m = new CModule(ast);
			DumpTAC(file, m);

			// TAC to intraproc CFG conversion
			CfgIntraProc *cfg_intra = new CfgIntraProc(m);
			DumpCfgIntraProc(file, cfg_intra);
			delete cfg_intra;

			// TAC to interproc CFG conversion
			CfgInterProc *cfg_inter = new CfgInterProc(m);
			DumpCfgInterProc(file, cfg_inter);

			// output x86 assembly to console or file
			DumpASM(file, m, NoOpt);

			// constant propagation
			if (do_const) {
				// TODO: do this from C_Propagation constructor
				const vector<shared_ptr<CfgProc>> &procs = cfg_inter->GetProcs();
				for (size_t p = 0; p < procs.size(); ++p) {
					// reaching-definition analysis
					procs[p]->ReachAlgo(); // for constant propagation
				}
				cout << "--------------------------------------------" <<endl;
				cout << "Constant propagation" << endl;
				cout << "--------------------------------------------" <<endl;
				C_Propagation *constant_propagation = new C_Propagation(cfg_inter);
				file += ".const";
				DumpTAC(file, m);
				DumpCfgInterProc(file, cfg_inter);
				DumpASM(file, m, ConstOpt);
			}

			// dead code elimination
			if (do_dead) {
				// TODO: do this from D_Elimination constructor
				const vector<shared_ptr<CfgProc>> &procs = cfg_inter->GetProcs();
				for (size_t p = 0; p < procs.size(); ++p) {
					// liveness analysis
					procs[p]->LiveAlgo(); // for dead code elimination
				}
				cout << "--------------------------------------------" <<endl;
				cout << "Dead code elimination" << endl;
				cout << "--------------------------------------------" <<endl;
				D_Elimination *deadcode_elimination = new D_Elimination(cfg_inter);
				file += ".dead";
				DumpTAC(file, m);
				DumpCfgInterProc(file, cfg_inter);
				if (do_const) DumpASM(file, m, FinOpt);
				else DumpASM(file, m, DeadOpt);
			}

			delete cfg_inter;
			delete m;
		}
	}

	return EXIT_SUCCESS;
}
