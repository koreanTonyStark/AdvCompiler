/* Constant-Propagation based on CFG
 * Author : team4 
 * Key Concept : changing .mod (with constant propagation)
 * Basic : skip array first (in implementation)
 */ 

//constant propagation 
//what about copy-propagation ?
//common sub-expression elimination 

#include <vector>
#include <memory>
#include <cassert>
#include <iostream>

#include "constant_propagation.h"

using namespace std;

using citCfgNode = list<shared_ptr<CfgNode>>::const_iterator;
using itCfgNode = list<shared_ptr<CfgNode>>::iterator;
using itCfgProc = vector<shared_ptr<CfgProc>>::iterator;

C_Propagation::C_Propagation(CfgInterProc *cfg)
{
	_cfg = cfg;
	_num_of_int  = 0;
	_num_of_bool = 0;
	_num_of_char = 0;
	_isExistConstFunc=false;
	_m = cfg->GetCModule(); 
	_symtab = _m->GetSymbolTable();	
	_procs = cfg->GetProcs();
	for(int i=0; i<_procs.size();++i)
		_num_of_code_lines+=_procs[i]->GetNodeCnt();
	cntNumOfVariables();
	//do constant propagation first 
	//second erase the code line by dead-code elimination
	doConstantPropagation();
	doInterProceduralConstantPropagation();
	if(_isExistConstFunc)
		doConstantPropagation();
}

int C_Propagation::returnInstanceTypeForCTacAddr(CTacAddr *addr)
{
	// enum Type{
	// 	NAME=0,
	// 	CONSTANT=1,
	// 	LABEL,
	// };

	if(CTacName* v =dynamic_cast<CTacName*>(addr)){
		/*
		// check if array
		const CSymbol* symbol = v->GetSymbol();
		CType* dataType = const_cast<CType*>(symbol->GetDataType());
		if (dynamic_cast<CArrayType*>(dataType) == NULL)
		*/
			return NAME;
	}
	else if(CTacConst* v =dynamic_cast<CTacConst*>(addr))
		return CONSTANT;
	else
		return LABEL;
}


shared_ptr<CfgNode> C_Propagation::hasOnlyOneReachbleLine(shared_ptr<CfgNode>& node, int idx)
{
	
	CfgNode::REACH &reach = node->GetReachInfo();
	set<shared_ptr<CfgNode>>::iterator it = reach._reachIn.begin();
	int cnt=0;
	size_t line_number=-1;
	shared_ptr<CfgNode> target_node;
	while(it!=reach._reachIn.end())
	{
		 
		CTacInstr *inst      = const_cast<CTacInstr*>(node->GetInstr());
		CTacName *name       = dynamic_cast<CTacName*>(inst->GetSrc(idx));
		CSymbol *symbol      = const_cast<CSymbol*>(name->GetSymbol());
		string symbol_name   = symbol->GetName();

		
		CTacInstr *comp_inst = const_cast<CTacInstr*>((*it)->GetInstr());
		if(comp_inst==nullptr) continue;
		CTacName *comp       = dynamic_cast<CTacName*>(comp_inst->GetDest());
		CSymbol *comp_symbol = const_cast<CSymbol*>(comp->GetSymbol());
		string comp_name     = comp_symbol->GetName();
		cout<<endl;
		cout<<" my : "<<symbol_name<<" target : "<<comp_name<<" ( in line "<<comp_inst->GetId()<<") "<<endl;
		if(symbol_name == comp_name)
		{
				target_node = *it;
				line_number=comp_inst->GetId();
				cnt++;
		}
		it++;
	}
	if(cnt==1)
		return target_node;
	
	else
		return nullptr;
}



void C_Propagation::ChangeToConstInOneLine(CTacInstr *target_inst, shared_ptr<CfgNode>& node, int idx)
{
	shared_ptr<CfgNode> target_node = hasOnlyOneReachbleLine(node, idx);
	if(target_node==nullptr)
		return;
	CTacInstr *target_instr = const_cast<CTacInstr*>(target_node->GetInstr());

	size_t     my_line = target_inst->GetId();
	CCodeBlock *cb = node->GetOwner()->GetCCodeBlock();
	cb->setInstr(my_line, target_instr, idx);
}

//binary operation 
int C_Propagation::GetOperationResult(EOperation target_op, int val1, int val2)
{
	
	int result;
	switch(target_op)
	{
		case opAdd:
			result = val1 + val2;
			break;
		case opSub:
			result = val1 - val2;
			break;
		case opMul:
			result = val1 * val2;
			break;
		case opDiv:
			result = val1 / val2;
			break;
		case opAnd:
			result = val1 & val2;
			break;
		case opOr:
			result = val1 | val2;
			break;
		default:
			break;
	}
	return result;
}

//unary operation 
int C_Propagation::GetOperationResult(EOperation target_op, int val1)
{
	int result;
	switch(target_op)
	{
		case opNeg:
			result = -val1;
			break;
		case opPos:
			result = +val1;
			break;
		case opNot:
			result = ~val1;
			break;
		default:
			break;
	}
	return result;
}


void C_Propagation::doConstantPropagation(void)
{
	//reaching definition -> in, out stores code line number 
	//simple algorithm -> very intuitive 
	/* if we have assignee in any node,
	(which means assignment block and we have to modfiy variable to constant)
	   we check that assignee's variable name and check whether there exists 
	   only 1 code_line(definition of assignee) for that assignee
	   then we can change it to constant through that line's constant 
	 */
	//No opSym in .mod 

	itCfgProc proc_it = _procs.begin();
	for(;proc_it<_procs.end();++proc_it)
	{
		const list<shared_ptr<CfgNode>>& nodeList_perProc = (*proc_it)->GetNodes();
		citCfgNode cit = nodeList_perProc.cbegin();

		while(cit!= nodeList_perProc.cend())
		{
			shared_ptr<CfgNode> node = (*cit);
			//only check has assignment to some variable 
			if(!(*cit)->GetUse().empty())
			{
				CTacInstr *target_inst= const_cast<CTacInstr*>(node->GetInstr());
				CTacAddr *src1 = target_inst->GetSrc(1);
				CTacAddr *src2 = target_inst->GetSrc(2);
				int num_src=target_inst->GetNumSrc();
				//# of src 0 : label
				//# of src 1 : unary operation and etc..(find it)
				//# of src 2 : binary operation 
				//binary operation :
				if(num_src==2)
				{
					cout<<(*proc_it)->GetName();
					cout<<" code line num : "<<target_inst->GetId();
					//if src is already const, then we don't need to handle about it
					//src1 is CTacName(CTacTemp , not CTacReference) -> must handle later
					if(src1->GetType()==CTacNameType)
					{

							CTacName *src1_name = dynamic_cast<CTacName*>(src1);
							if(!src1_name->GetSymbol()->GetDataType()->IsArray() && 
								!src1_name->GetSymbol()->GetDataType()->IsPointer())
								ChangeToConstInOneLine(target_inst, node, 1);
					} 
					if(src2->GetType()==CTacNameType)
					{
							CTacName *src2_name = dynamic_cast<CTacName*>(src2);
							if(!src2_name->GetSymbol()->GetDataType()->IsArray() &&
								!src2_name->GetSymbol()->GetDataType()->IsPointer())
								ChangeToConstInOneLine(target_inst, node, 2);
					}
					size_t my_id = target_inst->GetId();
					CTacAddr *new_src1= target_inst->GetSrc(1);
					CTacAddr *new_src2= target_inst->GetSrc(2);
					EOperation target_op = target_inst->GetOperation();
					if(target_op<=opOr)
					{
						if(returnInstanceTypeForCTacAddr(new_src1)==CONSTANT 
							&& returnInstanceTypeForCTacAddr(new_src2)==CONSTANT)
						{
							CTacConst *op1_instance = dynamic_cast<CTacConst*>(new_src1);
							CTacConst *op2_instance = dynamic_cast<CTacConst*>(new_src2);
							int val1 = op1_instance->GetValue();
							int val2 = op2_instance->GetValue();
							int result = GetOperationResult(target_op, val1, val2);
							
							cout<<"[val1 : "<<val1<<" val2: "<<val2<<" result :"<<result<<"]";
							
							target_inst->SetOperation(opAssign);
							CTacAddr *newConst = new CTacConst(result);
							target_inst->SetSrc1(newConst);
							target_inst->SetSrc2(nullptr);
						}
					}
				}
				//unary operation or assign or pointer operation 
				else if(num_src==1)
				{
					//constant propagation 
					CTacAddr *src1 = target_inst->GetSrc(1);
					cout<<"code line num : "<<target_inst->GetId();
					//name
					if(returnInstanceTypeForCTacAddr(src1)==NAME)
					{
							CTacName *src1_name = dynamic_cast<CTacName*>(src1);
							if(!src1_name->GetSymbol()->GetDataType()->IsArray() &&
								!src1_name->GetSymbol()->GetDataType()->IsPointer())
								ChangeToConstInOneLine(target_inst, node, 1);
					}

					EOperation target_op = target_inst->GetOperation();
					if(target_op<=8)  // means unary operation 
					{
						CTacAddr *new_src1 = target_inst->GetSrc(1);
						//check whether operand is constant 
						//if it's true than compute it on compile time and change it to assign operation 
						if(returnInstanceTypeForCTacAddr(new_src1)==CONSTANT)
						{
							CTacConst *op1_instance = dynamic_cast<CTacConst*>(new_src1);
							int val1 = op1_instance->GetValue();
							int result = GetOperationResult(target_op, val1);

							cout<<"[val1 : "<<val1<<" result: "<<result<<"]";
							target_inst->SetOperation(opAssign);
							//make EOPeration type to opAssign(9)
							
							CTacAddr *newConst = new CTacConst(result);
							target_inst->SetSrc1(newConst);
							target_inst->SetSrc2(nullptr);
						}
					}
				}
				cout<<endl;
			}
			cit++;
		}
	}
}


void C_Propagation::findConstantFunction(void)
{

	//main function's name 
	string main_func_name = _cfg->GetName();

	
	int val = INT_MIN;

	itCfgProc proc_it = _procs.begin();
	for(;proc_it<_procs.end();++proc_it)
	{
		//find a function that returns constant -> changing flag 

		int cnt = 0;	
		string target_name = (*proc_it)->GetName();
		
		
		if(main_func_name==target_name)
			continue;

		const list<shared_ptr<CfgNode>>& nodeList_perProc=(*proc_it)->GetNodes();
		citCfgNode cit = nodeList_perProc.cbegin();

		//traverse each procedure using instruction with incrementing 1
		while(cit!=nodeList_perProc.cend())
		{
			shared_ptr<CfgNode> node = *cit;

			CTacInstr *instr = const_cast<CTacInstr*>(node->GetInstr());

			if(instr->GetOperation()==opReturn)
			{	
				//case of opReturn 
				//we know it has only 1 src operand 
				CTacAddr * operand = instr->GetSrc(1);
				//not just case of return; 
				if(operand!=nullptr)
				{
					if(returnInstanceTypeForCTacAddr(operand)==CONSTANT)
					{
						cnt++;
						CTacConst* const_instance=dynamic_cast<CTacConst*>(operand);
						val = const_instance->GetValue();
						if(cnt==1)
						{
							_isExistConstFunc=true;
							(*proc_it)->SetReturnsConst(true);
							(*proc_it)->SetReturnVal(val);
							//cout<<target_name<<endl;

						}
						//cases of return CONST more than 1
						if(cnt>1 && val!=const_instance->GetValue())
							(*proc_it)->SetReturnsConst(false);
					}
					else
					{
						_isExistConstFunc=false;
						break;
					}
				}	
			}
			cit++;
		}
	}	
}


void C_Propagation::doInterProceduralConstantPropagation(void)
{
	findConstantFunction();
	if(_isExistConstFunc)
	{
		itCfgProc proc_it = _procs.begin();
		string main_func_name = _cfg->GetName();

		int cnt=0;
		//erase that function 
		for(;proc_it<_procs.end();++proc_it)
		{

			string target_name=(*proc_it)->GetName();
			cout<<target_name<<" ";
			if((*proc_it)->GetReturnsConst())
			{
				int val = (*proc_it)->GetReturnVal();
				CScope *parent = (*proc_it)->GetCCodeBlock()->GetOwner()->GetParent();
				cout<<parent->GetName()<<endl;
				vector<CScope*>& child = const_cast<vector<CScope*>&>(parent->GetSubscopes());
				
				//erase function block first
				for(int i=0; i<child.size();++i)
				{
					cout<<child[i]->GetName()<<endl;
					if(target_name==child[i]->GetName())
					{
						child.erase(child.begin()+i);
						break;
					}

				}


				//erase line on child procedure
				vector<CScope*>& new_child = const_cast<vector<CScope*>&>(parent->GetSubscopes());
				
				for(int i=0; i<new_child.size();++i)
				{
					//change it it's main function del param and change opCall to opAssign
					CCodeBlock *cb = new_child[i]->GetCodeBlock();
					list<CTacInstr*> instr_list = const_cast<list<CTacInstr*>&>(cb->GetInstr());
					

					list<CTacInstr*>::reverse_iterator rit = instr_list.rbegin();
					bool find_function=false;
					while(rit!=instr_list.rend())
					{
						CTacInstr *inst = *rit;
						if(find_function==false)
						{
							if(inst->GetOperation()==opCall)
							{
								CTacAddr* function_name = inst->GetSrc(1);
								if(returnInstanceTypeForCTacAddr(function_name)==NAME)
								{
									CTacName* comp_name = dynamic_cast<CTacName*>(function_name);
									CSymbol* comp_symbol = const_cast<CSymbol*>(comp_name->GetSymbol());
									string   comp_string = comp_symbol->GetName();
									if(target_name==comp_string)
									{
										inst->SetOperation(opAssign);
										CTacAddr *newConst = new CTacConst(val);
										inst->SetSrc1(newConst);
										inst->SetSrc2(nullptr);
										find_function=true;
										rit++;
										continue;
									}
								}
							}
						}

						if(find_function==true)
						{
							if(inst->GetOperation()==opParam)
							{
								cout<<inst->GetId()<<endl;
								cb->DelInstr(inst->GetId());			
							}
							else
								find_function=false;

						}
						rit++;
					}


				}

				//erase line on main procedure
				CCodeBlock *main_cb = parent->GetCodeBlock();
				list<CTacInstr*> instr_list = const_cast<list<CTacInstr*>&>(main_cb->GetInstr());

				list<CTacInstr*>::reverse_iterator rit = instr_list.rbegin();
					bool find_function=false;
					while(rit!=instr_list.rend())
					{
						CTacInstr *inst = *rit;
						if(find_function==false)
						{
							if(inst->GetOperation()==opCall)
							{
								CTacAddr* function_name = inst->GetSrc(1);
								if(returnInstanceTypeForCTacAddr(function_name)==NAME)
								{
									CTacName* comp_name = dynamic_cast<CTacName*>(function_name);
									CSymbol* comp_symbol = const_cast<CSymbol*>(comp_name->GetSymbol());
									string   comp_string = comp_symbol->GetName();
									if(target_name==comp_string)
									{
										inst->SetOperation(opAssign);
										CTacAddr *newConst = new CTacConst(val);
										inst->SetSrc1(newConst);
										inst->SetSrc2(nullptr);
										find_function=true;
										rit++;
										continue;
									}
								}
							}
						}

						if(find_function==true)
						{
							if(inst->GetOperation()==opParam)
							{
								cout<<inst->GetId()<<endl;
								main_cb->DelInstr(inst->GetId());			
							}
							else
								find_function=false;

						}
						rit++;
					}

				
			}
			cnt++;
		}
	}	
}


C_Propagation::~C_Propagation()
{
}



void C_Propagation::showNumOfPrimitive(void) const
{
	cout<<"number of INT  variable : "<<_num_of_int<<endl;
	cout<<"number of BOOL variable : "<<_num_of_bool<<endl;
	cout<<"number of CHAR variable : "<<_num_of_char<<endl;
}

CfgInterProc* C_Propagation::getCFG(void) const
{
	return _cfg;
}

const CSymtab* C_Propagation::getCSymtab(void) const
{
	return _symtab;
}

size_t C_Propagation::getNumOfInt(void) const
{
	return _num_of_int;
} 

size_t C_Propagation::getNumOfBool(void) const
{
	return _num_of_bool;
} 
size_t C_Propagation::getNumOfChar(void) const
{
	return _num_of_char;
} 
size_t C_Propagation::getNumOfCodeBlocks(void) const
{
	return _num_of_code_lines;
}

void C_Propagation::cntNumOfVariables(void)
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





