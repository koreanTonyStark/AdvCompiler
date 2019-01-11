/* Constant-Propagation based on CFG
 * Author : team4 
 * Key Concept : changing .mod (with constant propagation)
 * Basic : skip array first (in implementation)
 */ 

//constant propagation 
//common-subexpression elimination 

#include <vector>
#include <memory>
#include <cassert>
#include <iostream>

#include "deadcode_elimination.h"

using namespace std;

using citCfgNode = list<shared_ptr<CfgNode>>::const_iterator;
using itCfgNode = list<shared_ptr<CfgNode>>::iterator;
using itCfgProc = vector<shared_ptr<CfgProc>>::iterator;

D_Elimination::D_Elimination(CfgInterProc *cfg)
{
	_cfg = cfg;
	_num_of_int  = 0;
	_num_of_bool = 0;
	_num_of_char = 0;
	_m = cfg->GetCModule(); 
	_symtab = _m->GetSymbolTable();	
	_procs = cfg->GetProcs();
	for(int i=0; i<_procs.size();++i)
		_num_of_code_lines+=_procs[i]->GetNodeCnt();
	cntNumOfVariables();
	//dead-code elimination
	doDeadCodeElimination();

	
}



void D_Elimination::doDeadCodeElimination(void)
{
	//store list of instructions which is definition 
	//we can check a<-b if a is in LiveOut on that list 
	//if not, then erase, if is then live 
	// no use but keep for urgency: list<shared_ptr<CfgNode>> def_list;
	itCfgProc proc_it = _procs.begin();
	for(;proc_it<_procs.end();++proc_it)
	{
		const list<shared_ptr<CfgNode>>& nodeList_perProc = (*proc_it)->GetNodes();
		citCfgNode cit = nodeList_perProc.cbegin();
		while(cit!= nodeList_perProc.cend())
		{
			shared_ptr<CfgNode> node = (*cit);
			//only check has assignment to some variable 
			if((*cit)->GetDef()!=nullptr)
			{
				
				CTacAddr *var = node->GetDef();
				CfgNode::LIVE &live = node->GetLiveInfo();
				//dead-code found : can't find var in liveOut
				set<CTacAddr*>::iterator tacit=live._liveOut.begin();
				CTacName *var_name = dynamic_cast<CTacName*>(var);
				CSymbol *var_name_symbol = const_cast<CSymbol*>(var_name->GetSymbol());
				string name_of_def = var_name_symbol->GetName();
				bool dead_flag=true;

				while(tacit!=live._liveOut.end())
				{
					CTacAddr *adr = *tacit;	
					if(CTacName *v = dynamic_cast<CTacName*>(adr))
					{

						CTacName *comp_name = dynamic_cast<CTacName*>(adr);
						CSymbol *comp_name_symbol = const_cast<CSymbol*>(comp_name->GetSymbol());
						string name_of_comp = comp_name_symbol->GetName();
						if(name_of_def==name_of_comp)
						{
							dead_flag=false;
							break;
						}
					}
					tacit++;
				}
				if(dead_flag)
				{
					cout<<"dead-code found on line number"<< node->GetId()<<endl;
					CTacInstr* target = const_cast<CTacInstr*>(node->GetInstr());
					size_t target_id = target->GetId();
					CCodeBlock* cb = (*proc_it)->GetCCodeBlock();
					cb->DelInstr(target_id);
					//-----added for cfg----------
					(*(proc_it))->DelNode(*(cit)++);
						continue;
					//----------------------------


				}
			}
			cit++;
		}

	}


	
}




D_Elimination::~D_Elimination()
{
}


void D_Elimination::showNumOfPrimitive(void) const
{
	cout<<"number of INT  variable : "<<_num_of_int<<endl;
	cout<<"number of BOOL variable : "<<_num_of_bool<<endl;
	cout<<"number of CHAR variable : "<<_num_of_char<<endl;
}

CfgInterProc* D_Elimination::getCFG(void) const
{
	return _cfg;
}

const CSymtab* D_Elimination::getCSymtab(void) const
{
	return _symtab;
}

size_t D_Elimination::getNumOfInt(void) const
{
	return _num_of_int;
} 

size_t D_Elimination::getNumOfBool(void) const
{
	return _num_of_bool;
} 
size_t D_Elimination::getNumOfChar(void) const
{
	return _num_of_char;
} 
size_t D_Elimination::getNumOfCodeBlocks(void) const
{
	return _num_of_code_lines;
}

void D_Elimination::cntNumOfVariables(void)
{
	const vector<CSymbol*> &list = _symtab->GetSymbols();
	for(int i=0; i<list.size(); ++i)
	{
		const CType* type = list[i]->GetDataType();
		if(type->IsBoolean())
			_num_of_bool++;
		else if(type->IsChar())
			_num_of_char++;
		else if(type->IsInt())
			_num_of_int++;
	}
}





