/* Constant-Propagation based on CFG
 * Author : team4 
 * Key Concept : changing .mod (with constant propagation)
 * Basic : skip array first (in implementation)
 */ 

#include "constant_propagation.h"

using namespace std;

C_Propagation::C_Propagation(CfgInterProc *cfg)
{
	_cfg = cfg;
	_num_of_int  = 0;
	_num_of_bool = 0;
	_num_of_char = 0;
	CModule *_m = cfg->GetCModule(); 
	CSymtab *_symtab = _m->GetSymbolTable();
	const vector<CSymbol*> &list = _symtab->GetSymbols();
	for(int i=0; i<list.size(); ++i)
	{
		cout<<"name: "<<list[i]->GetName()<<" ";
		cout<<"symbol type: "<<list[i]->GetSymbolType()<<" ";
		cout<<list[i]->GetDataType()<<" ";
		const CType* type = list[i]->GetDataType();
		if(type->IsBoolean())
			_num_of_bool++;
		else if(type->IsChar())
			_num_of_char++;
		else if(type->IsInt())
			_num_of_int++;
		cout<<"data : ";
		if(list[i]->GetData()!=nullptr)
			cout<<list[i]->GetData();
		cout<<"base register: "<<list[i]->GetBaseRegister()<<" ";
		cout<<"offset(?): "<<list[i]->GetOffset()<<endl;

	}
	cout<<_num_of_int<<" "<<_num_of_char<<" "<<_num_of_bool<<endl;

	//CSymtab& _symtab =_cfg->_m->_symtab;
	
}

C_Propagation::~C_Propagation()
{
}


