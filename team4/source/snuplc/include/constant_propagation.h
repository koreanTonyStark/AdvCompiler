#ifndef __CONSTANT_PROPAGATION__
#define __CONSTANT_PROPAGATION__

#include <iostream>
#include <vector>
#include <memory>
#include <list>

#include "cfg.h"

class C_Propagation
{

public:
	enum Type{
		NAME=0,
		CONSTANT,
		LABEL,
	};
	C_Propagation(CfgInterProc *cfg);
	virtual ~C_Propagation();
	CfgInterProc*       getCFG(void)             const;
	const CSymtab*      getCSymtab(void)         const;
	size_t              getNumOfInt(void)  	     const;
	size_t              getNumOfBool(void)       const;
	size_t              getNumOfChar(void)       const;
	size_t              getNumOfCodeBlocks(void) const;
	//don't have to define setFunction to above 3 item 
	void                cntNumOfVariables(void);
	void                showNumOfPrimitive(void) const;
	void                doConstantPropagation(void);
	shared_ptr<CfgNode> hasOnlyOneReachbleLine(shared_ptr<CfgNode>& node, int idx);
	int                 returnInstanceTypeForCTacAddr(CTacAddr *addr);
	void                ChangeToConstInOneLine(CTacInstr *target_inst, shared_ptr<CfgNode>& node, int idx);
	int                 GetOperationResult(EOperation target_op, int val1, int val2);
	int                 GetOperationResult(EOperation target_op, int val1);
	void                findConstantFunction(void);
	void                doInterProceduralConstantPropagation(void);
protected:
	bool _isExistConstFunc;
	CfgInterProc *_cfg;
	CModule *_m;
	CSymtab *_symtab;
	vector<shared_ptr<CfgProc>> _procs;
	size_t _num_of_int;
	size_t _num_of_bool;
	size_t _num_of_char;
	size_t _num_of_code_lines;
};

#endif 
