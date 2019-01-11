#ifndef __DEADCODE_ELIMINATION__
#define __DEADCODE_ELIMINATION__

#include <iostream>
#include <vector>
#include <memory>
#include <list>

#include "cfg.h"

class D_Elimination
{

public:
	D_Elimination(CfgInterProc *cfg);
	virtual ~D_Elimination();
	CfgInterProc*       getCFG(void)             const;
	const CSymtab*      getCSymtab(void)         const;
	size_t              getNumOfInt(void)  	     const;
	size_t              getNumOfBool(void)       const;
	size_t              getNumOfChar(void)       const;
	size_t              getNumOfCodeBlocks(void) const;
	//don't have to define setFunction to above 3 item 
	void                cntNumOfVariables(void);
	void                showNumOfPrimitive(void) const;
	//void                livenessAnalysis(void);
	void                doDeadCodeElimination(void);
	
protected:
	CfgInterProc *_cfg;
	CModule *_m;
	CSymtab *_symtab;
	vector<shared_ptr<CfgProc>> _procs;
	size_t _num_of_int;
	size_t _num_of_bool;
	size_t _num_of_char;
	size_t _num_of_code_lines;
	//vector<shared_ptr<CfgNode>> _def_list;
	// <var, data> data-structure 

};



#endif 
