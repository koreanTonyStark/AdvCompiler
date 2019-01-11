#ifndef __CONSTANT_PROPAGATION__
#define __CONSTANT_PROPAGATION__

#include <iostream>

#include "cfg.h"

class C_Propagation
{
public:
	C_Propagation(CfgInterProc *cfg);
	virtual ~C_Propagation();
	//with each variable or just one call ? 
	void doConstantPropagation();
	size_t cntNumOfVaraibles();



protected:
	CfgInterProc *_cfg;
	size_t _num_of_int;
	size_t _num_of_bool;
	size_t _num_of_char;
	// <var, data> data-structure 


};



#endif 