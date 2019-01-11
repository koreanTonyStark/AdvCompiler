/*
 * cfg.cpp
 *
 *      Author: team4
 */

#include <cassert>
#include <algorithm>

#include "cfg.h"

//------------------------------------------------------------------------------
// iterators
//

using citCfgNode = list<shared_ptr<CfgNode>>::const_iterator;
using critCfgNode = list<shared_ptr<CfgNode>>::const_reverse_iterator;
using itCfgNode = list<shared_ptr<CfgNode>>::iterator;
using ritCfgNode = list<shared_ptr<CfgNode>>::reverse_iterator;
using citCTacInstr = list<CTacInstr*>::const_iterator;
using setCitCTacAddr = set<CTacAddr*>::const_iterator;
using setCitCfgNode = set<shared_ptr<CfgNode>>::const_iterator;
using mapItCTacAddrCfgNode = map<CTacAddr*, shared_ptr<CfgNode>, CTacAddrCmp>::iterator;

//------------------------------------------------------------------------------
// CfgNodeCmp
//

CfgNodeCmp::CfgNodeCmp(void) {
}

bool CfgNodeCmp::operator()(const shared_ptr<CfgNode> &lhs,
		const shared_ptr<CfgNode> &rhs) const {
	if (!lhs || !rhs)
		return false;
	return lhs->GetId() < rhs->GetId();
}

//------------------------------------------------------------------------------
// CfgNode
//

CfgNode::CfgNode(CfgProc *owner, CTacInstr *instr) {
	assert(owner != NULL);
	assert(instr != NULL);
	if (!owner || !instr)
		return;
	_owner = owner;
	_id = owner->GetNodeCnt() + owner->GetNodeOffset();
	_instr = instr;
	InitNode();
}

CfgNode::CfgNode(const CfgNode &node) {
	_owner = node._owner;
	_id = node._id;
	_instr = node._instr;
	InitNode();
}

CfgNode::~CfgNode(void) {

}

const size_t CfgNode::InDegree(void) const {
	return _preds.size();
}

const size_t CfgNode::OutDegree(void) const {
	return _succs.size();
}

bool CfgNode::GoesTo(const shared_ptr<CfgNode> &n) const {
	if (find(_succs.begin(), _succs.end(), n) != _succs.end())
		return true;
	return false;
}

bool CfgNode::ComesFrom(const shared_ptr<CfgNode> &n) const {
	if (find(_preds.begin(), _preds.end(), n) != _preds.end())
		return true;
	return false;
}

void CfgNode::AddSucc(const shared_ptr<CfgNode> &n) {
	if (!GoesTo(n))
		_succs.push_back(n);
}

void CfgNode::AddPred(const shared_ptr<CfgNode> &n) {
	if (!ComesFrom(n))
		_preds.push_back(n);
}

void CfgNode::RmSucc(const shared_ptr<CfgNode> &n) {
	if (GoesTo(n))
		_succs.remove(n);
}

void CfgNode::RmPred(const shared_ptr<CfgNode> &n) {
	if (ComesFrom(n))
		_preds.remove(n);
}

bool CfgNode::VarIsGlobal(CTacAddr* var) const {
	const vector<string> &globals = _owner->GetGlobals();
	CTacName* candidate = dynamic_cast<CTacName*>(var);
	if (candidate) {
		const string &name = candidate->GetSymbol()->GetName();
		for (size_t i = 0; i < globals.size(); ++i) {
			if(name == globals[i])
				return true;
		}
	}
	return false;
}

void CfgNode::InitNode(void) {
	// if re-initialized
	_def = nullptr;
	if (!_use.empty())
		_use.clear();
	//_globalInfo._preds.empty();
	//_globalInfo._succs.empty();

	// initialize
	_def = dynamic_cast<CTacAddr*>(_instr->GetDest());

	unsigned int numSrc = _instr->GetNumSrc();
	if (numSrc > 0) {
		_use.push_back(_instr->GetSrc(1));
		if (numSrc > 1) {
			_use.push_back(_instr->GetSrc(2));
		}
	}

	EOperation op = _instr->GetOperation();
	switch (op) {
	case opParam:
		_def = nullptr; // we don't need param index in _def
		break;
	case opCall:
		_use.clear(); // we don't need func name in _use
		break;
	case opGoto: {
		if (!IsRelOp(op))
			_def = nullptr; // we don't need jump label in _def
		break;
	}
	case opAssign: {
		if (dynamic_cast<CTacReference*>(_instr->GetDest())) {
			_use.push_back(_def); // reference is in _use
			_def = nullptr; // reference is not in _def
		}
		break;
	}
	// skip for now
/*	case opAddress:
	case opDeref:
	case opCast: {
		_use.clear();
		_def = nullptr;
		break;
	}*/
	}

	// initialize global variables
	if (_def) {
		if (VarIsGlobal(_def)) {
			_global.insert(_def);
		}
	}
	for (size_t i = 0; i < _use.size(); ++i){
		//if (_use[i]->equal_to(*_def))
			//continue;
		if (VarIsGlobal(_use[i])){
			_global.insert(_use[i]);
			//_liveInfo._liveIn.insert(_use[i]);
		}
	}
}

//------------------------------------------------------------------------------
// CfgProc
//

CfgProc::CfgProc(CCodeBlock *cb, size_t offset, vector<string> &globals) {
	assert(cb != NULL);
	if (!cb)
		return;
	_cb = cb;
	_name = cb->GetName();
	_offset = offset;
	_globals.assign(globals.begin(), globals.end());
	_ReturnsConst = false;
	_ReturnVal = INT_MIN;
	//_parentFuncName=; GetCodeBlock()->GetOwner()->GetParent()->GetName();
	MakeNodes();
	MakeEdges();
}

CfgProc::CfgProc(const CfgProc &proc) {
	_cb = proc._cb;
	_name = proc._name;
	_offset = proc._offset;
	_globals.assign(proc._globals.begin(), proc._globals.end());
	_ReturnsConst = proc._ReturnsConst;
	_ReturnVal = proc._ReturnVal;
	//_parentFuncName = 
	// make new copies of existing nodes
	for (citCfgNode it = proc._nodes.cbegin(); it != proc._nodes.cend(); ++it) {
		const shared_ptr<CfgNode> &node = *it;
		shared_ptr<CfgNode> newNode(new CfgNode(*node));
		_nodes.push_back(newNode);
	}
	MakeEdges();
}

CfgProc::~CfgProc(void) {

}

const size_t CfgProc::GetNodeCnt(void) const {
	return _nodes.size();
}

const shared_ptr<CfgNode> CfgProc::FindNode(const CTacInstr *instr) const {
	for (citCfgNode it = _nodes.cbegin(); it != _nodes.cend(); ++it) {
		const shared_ptr<CfgNode> &n = *it;
		if (n->GetInstr() == instr)
			return n;
	}
	return nullptr;
}

void CfgProc::AddEdge(const shared_ptr<CfgNode> &from,
		const shared_ptr<CfgNode> &to) {
	to->AddPred(from);
	from->AddSucc(to);
}

void CfgProc::RmEdge(const shared_ptr<CfgNode> &from,
		const shared_ptr<CfgNode> &to) {
	to->RmPred(from);
	from->RmSucc(to);
}

void CfgProc::DelNode(const shared_ptr<CfgNode> &n) {
	if (n->GetOwner() == this) {
		size_t inDegree = n->InDegree();
		size_t outDegree = n->OutDegree();
		if (inDegree == 1 || outDegree == 1) {
			const list<shared_ptr<CfgNode>> &preds = n->GetPreds();
			const list<shared_ptr<CfgNode>> &succs = n->GetSuccs();
			const shared_ptr<CfgNode> &from = preds.front();
			const shared_ptr<CfgNode> &to = succs.front();
			if (outDegree == 1) {
				RmEdge(n, to);
			}
			if (inDegree == 1) {
				RmEdge(from, n);
			}
			if (inDegree == 1 && outDegree == 1) {
				AddEdge(from, to);
			}
			_nodes.remove(n);
		}
	}
}

void CfgProc::toDot(ostream &out) const {
	out << "// scope '" << _name << "'" << endl;
	for (citCfgNode it = _nodes.cbegin(); it != _nodes.cend(); ++it) {
		const shared_ptr<CfgNode> &n = *it;

		size_t id = n->GetId();
		out << "node" << id << " [label=\"";
		if (n == _nodes.front()) {
			out << " ENTER " << _name << "\\r ";
		} else if (n == _nodes.back()) {
			out << " EXIT " << _name << "\\r ";
		}

		const CTacInstr *instr = n->GetInstr();
		out << instr << "\\l\",shape=box];" << endl;

		const size_t degree = n->OutDegree();
		if (degree > 0) {
			const list<shared_ptr<CfgNode>> &succs = n->GetSuccs();
			for (citCfgNode nit = succs.cbegin(); nit != succs.cend(); ++nit) {
				const shared_ptr<CfgNode> &next = *nit;
				size_t nid = next->GetId();
				out << "node" << id << " -> " << "node" << nid << ";" << endl;
			}
		}

		const set<shared_ptr<CfgNode>, CfgNodeCmp> global_succs =
				n->GetGlobalInfo()._succs;
		for (setCitCfgNode git = global_succs.cbegin();
				git != global_succs.cend(); ++git) {
			const shared_ptr<CfgNode> &global = *git;
			size_t gid = global->GetId();
			out << "node" << id << " -> " << "node" << gid << " [style=dotted];"
					<< endl;
		}
	}
}

void CfgProc::LiveAlgo(void) {
	// backward analysis
	cout << "--------------------------------------------" << endl;
	cout << "Liveness analysis of " << _name << endl;
	cout << "--------------------------------------------" << endl;

	critCfgNode rit = _nodes.crbegin(); // const reverse iterator
	shared_ptr<CfgNode> node = *rit;
	// initialize use and def for each node
	while (rit != _nodes.crend()) {
		node = *rit++;
		node->InitNode();
	}

	CfgProc *copy_proc = new CfgProc(*this);
	const list<shared_ptr<CfgNode>> &copy_nodes = copy_proc->GetNodes();
	critCfgNode copy_rit = copy_nodes.crbegin();
	shared_ptr<CfgNode> copy_node = *copy_rit;

	// print
	unsigned int step = 0;
	//DumpLive(step, copy_proc);

	// first iteration
	rit = _nodes.crbegin();
	while (rit != _nodes.crend()) {
		node = *rit++;
		LiveEq(node);
	}

	// print
	step++;
	DumpLive(step, this);

	// repeat until reaching fixed-point
	while (LiveFixPoint(copy_nodes)) {
		copy_rit = copy_nodes.crbegin();
		rit = _nodes.crbegin();
		while (copy_rit != copy_nodes.crend() && rit != _nodes.crend()) {
			node = *rit++;
			copy_node = *copy_rit++;
			CfgNode::LIVE &live = node->GetLiveInfo();
			CfgNode::LIVE &copy_live = copy_node->GetLiveInfo();
			// save
			copy_live._liveIn = live._liveIn;
			copy_live._liveOut = live._liveOut;
			// step
			LiveEq(node);
		}
		// print
		step++;
		DumpLive(step, this);
	}
	delete copy_proc;
}


void CfgProc::ReachAlgo(void) {
	// forward analysis
	cout << "--------------------------------------------" << endl;
	cout << "Reaching-definition analysis of " << _name << endl;
	cout << "--------------------------------------------" << endl;

	citCfgNode it = _nodes.cbegin();
	shared_ptr<CfgNode> node = *it;
	// initialize use and def for each node
	while (it != _nodes.cend()) {
		node = *it++;
		node->InitNode();
	}

	// initialize gen and kill for each node
	ReachDef();

	CfgProc *copy_proc = new CfgProc(*this);
	const list<shared_ptr<CfgNode>> &copy_nodes = copy_proc->GetNodes();
	citCfgNode copy_it = copy_nodes.cbegin();
	shared_ptr<CfgNode> copy_node = *copy_it;
	// print
	unsigned int step = 0;
	//DumpReach(step, this);

	// first iteration
	it = _nodes.cbegin();
	while (it != _nodes.cend()) {
		node = *it++;
		ReachEq(node);
	}

	// print
	step++;
	DumpReach(step, this);

	// repeat until reaching fixed-point
	while (ReachFixPoint(copy_nodes)) {
		copy_it = copy_nodes.cbegin();
		it = _nodes.cbegin();
		while (copy_it != copy_nodes.cend() && it != _nodes.cend()) {
			node = *it++;
			copy_node = *copy_it++;
			CfgNode::REACH &reach = node->GetReachInfo();
			CfgNode::REACH &copy_reach = copy_node->GetReachInfo();
			// save
			copy_reach._reachIn = reach._reachIn;
			copy_reach._reachOut = reach._reachOut;
			// step
			ReachEq(node);
		}
		// print
		step++;
		DumpReach(step, this);
	}
	delete copy_proc;
}

bool CfgProc::LiveFixPoint(const list<shared_ptr<CfgNode>> &copy_nodes) {
	critCfgNode rit = _nodes.crbegin();
	critCfgNode copy_rit = copy_nodes.crbegin();
	while (copy_rit != copy_nodes.crend() && rit != _nodes.crend()) {
		const shared_ptr<CfgNode> &node = *rit++;
		const shared_ptr<CfgNode> &copy_node = *copy_rit++;
		CfgNode::LIVE &live = node->GetLiveInfo();
		CfgNode::LIVE &copy_live = copy_node->GetLiveInfo();
		if (live._liveIn != copy_live._liveIn
				&& live._liveOut != copy_live._liveOut) {
			return true;
		}
	}
	return false;
}

void CfgProc::LiveEq(const shared_ptr<CfgNode>& node) {
	CfgNode::LIVE &live = node->GetLiveInfo();
	const list<shared_ptr<CfgNode>> &succs = node->GetSuccs();
	for (citCfgNode it = succs.cbegin(); it != succs.cend(); ++it) {
		const shared_ptr<CfgNode> &succ_node = *it;
		if (succ_node->GetOwner() == node->GetOwner()) {
			CfgNode::LIVE &succ_live = succ_node->GetLiveInfo();
			live._liveOut.insert(succ_live._liveIn.begin(),
					succ_live._liveIn.end());
		}
	}

/*	const set<shared_ptr<CfgNode>, CfgNodeCmp> &global_succs =
			node->GetGlobalInfo()._succs;
	for (setCitCfgNode it = global_succs.cbegin(); it != global_succs.cend(); ++it) {
		const shared_ptr<CfgNode> &succ_node = *it;
		CfgNode::LIVE &succ_live = succ_node->GetLiveInfo();
		live._liveOut.insert(succ_live._liveIn.begin(),
				succ_live._liveIn.end());
	}*/

	live._liveIn.insert(live._liveOut.begin(), live._liveOut.end());
	CTacAddr* def = node->GetDef();
	if (def) {
		live._liveIn.erase(def);
	}

	live._liveIn.insert(node->GetUse().begin(), node->GetUse().end());
}

void CfgProc::ReachDef(void) {
	list<shared_ptr<CfgNode>> defs; // list of all defs in this proc
	for (citCfgNode it = _nodes.cbegin(); it != _nodes.cend(); ++it) {
		const shared_ptr<CfgNode> &node = *it;
		if (node->GetDef()) {
			defs.push_back(node);
		}
		const set<shared_ptr<CfgNode>, CfgNodeCmp> &global_preds =
				node->GetGlobalInfo()._preds;
		for (setCitCfgNode it = global_preds.cbegin(); it != global_preds.cend(); ++it) {
			const shared_ptr<CfgNode> &pred_node = *it;
			CTacAddr *def = pred_node->GetDef();
			if(!def)
				continue;
			if (pred_node->VarIsGlobal(def))
				defs.push_back(pred_node);
		}
	}

	for (citCfgNode it = _nodes.cbegin(); it != _nodes.cend(); ++it) {
		const shared_ptr<CfgNode> &node = *it;
		CTacAddr* def = node->GetDef();
		if (def) {
			CfgNode::REACH &reach = node->GetReachInfo();
			reach._gen.insert(node);
			for (citCfgNode def_it = defs.cbegin(); def_it != defs.cend(); ++def_it) {
				const shared_ptr<CfgNode> &def_node = *def_it;
				CTacAddr* prev_def = def_node->GetDef();
				if (def->equal_to(*prev_def)) {
					if (prev_def != def) {
						reach._kill.insert(def_node);
					}
				}
			}
		}
	}
	DumpReachDef(this);
}

bool CfgProc::ReachFixPoint(const list<shared_ptr<CfgNode>> &copy_nodes) {
	citCfgNode it = _nodes.cbegin();
	citCfgNode copy_it = copy_nodes.cbegin();
	while (copy_it != copy_nodes.cend() && it != _nodes.cend()) {
		const shared_ptr<CfgNode> node = *it++;
		const shared_ptr<CfgNode> copy_node = *copy_it++;
		CfgNode::REACH &reach = node->GetReachInfo();
		CfgNode::REACH &copy_reach = copy_node->GetReachInfo();
		if (reach._reachIn != copy_reach._reachIn
				&& reach._reachOut != copy_reach._reachOut) {
			return true;
		}
	}
	return false;
}

void CfgProc::ReachEq(const shared_ptr<CfgNode>& node) {
	CfgNode::REACH &reach = node->GetReachInfo();
	const list<shared_ptr<CfgNode>> &preds = node->GetPreds();
	for (citCfgNode it = preds.cbegin(); it != preds.cend(); ++it) {
		const shared_ptr<CfgNode> &pred_node = *it;
		if (pred_node->GetOwner() == node->GetOwner()) {
			CfgNode::REACH &pred_reach = pred_node->GetReachInfo();
			reach._reachIn.insert(pred_reach._reachOut.cbegin(),
					pred_reach._reachOut.cend());
		}
	}

	const set<shared_ptr<CfgNode>, CfgNodeCmp> &global_preds =
			node->GetGlobalInfo()._preds;
	for (setCitCfgNode it = global_preds.cbegin(); it != global_preds.cend(); ++it) {
		const shared_ptr<CfgNode> &pred_node = *it;
		CfgNode::REACH &pred_reach = pred_node->GetReachInfo();
		reach._reachIn.insert(pred_reach._reachOut.cbegin(),
				pred_reach._reachOut.cend());
	}

	reach._reachOut.insert(reach._reachIn.begin(), reach._reachIn.end());
	for (setCitCfgNode it = reach._kill.cbegin(); it != reach._kill.cend(); ++it) {
		const shared_ptr<CfgNode> &kill_node = *it;
		reach._reachOut.erase(kill_node);
	}

	for (setCitCfgNode it = reach._gen.cbegin(); it != reach._gen.cend(); ++it) {
		const shared_ptr<CfgNode> &gen_node = *it;
		reach._reachOut.insert(gen_node);
	}
}

void CfgProc::DumpLive(const unsigned int step, const CfgProc *proc) const {
	cout << "Iteration : " << step << endl;
	cout << "NodeId\t| " << "succs\t| " << "use\t| " << "def\t| " << "out\t| "
			<< "in\n";
	const list<shared_ptr<CfgNode>> &nodes = proc->GetNodes();
	for (critCfgNode node_it = nodes.crbegin(); node_it != nodes.crend();
			++node_it) {
		const shared_ptr<CfgNode> &node = *node_it;
		//print node id
		size_t nodeId = node->GetId();
		cout << "n[" << nodeId << "]:\t| ";

		// print succs
		const list<shared_ptr<CfgNode>> &succs = node->GetSuccs();
		for (citCfgNode it = succs.cbegin(); it != succs.cend(); ++it) {
			const shared_ptr<CfgNode> &succ = *it;
			size_t succId = succ->GetId();
			cout << succId;
			if (succ != succs.back())
				cout << ",";
		}
		if (succs.empty())
			cout << "NULL";
		cout << "\t| ";

		// print use
		const vector<CTacAddr*> &use = node->GetUse();
		for (size_t i = 0; i < use.size(); ++i) {
			cout << use[i];
			if (i != use.size() - 1)
				cout << ",";
		}
		if (node->GetUse().empty()) {
			cout << "NULL";
		}
		cout << "\t| ";

		// print def
		CTacAddr *def = node->GetDef();
		if (def)
			cout << def << "\t| ";
		else
			cout << "NULL" << "\t| ";

		CfgNode::LIVE &live = node->GetLiveInfo();
		// print liveOut
		for (setCitCTacAddr it = live._liveOut.cbegin();
				it != live._liveOut.cend(); ++it) {
			CTacAddr *def = *it;
			cout << def;
			if (def != *live._liveOut.crbegin())
				cout << ",";
		}
		if (live._liveOut.empty())
			cout << "NULL";
		cout << "\t| ";

		// print liveIn
		for (setCitCTacAddr it = live._liveIn.cbegin();
				it != live._liveIn.cend(); ++it) {
			CTacAddr *def = *it;
			cout << def;
			if (def != *live._liveIn.crbegin())
				cout << ",";
		}
		if (live._liveIn.empty())
			cout << "NULL";
		cout << "\n";
	}
	cout << endl;
}

void CfgProc::DumpReachDef(const CfgProc *proc) const {
	cout << "NodeId\t| " << "def\t| " << "gen\t| " << "kill\n";
	const list<shared_ptr<CfgNode>> &nodes = proc->GetNodes();
	for (citCfgNode node_it = nodes.cbegin(); node_it != nodes.cend();
			++node_it) {
		const shared_ptr<CfgNode> &node = *node_it;
		// print node id
		size_t nodeId = node->GetId();
		cout << "n[" << nodeId << "]:\t| ";

		//print def
		CTacAddr *def = node->GetDef();
		if (def)
			cout << def << "\t| ";
		else
			cout << "NULL" << "\t| ";

		CfgNode::REACH &reach = node->GetReachInfo();
		// print gen
		for (setCitCfgNode it = reach._gen.cbegin(); it != reach._gen.cend(); ++it) {
			const shared_ptr<CfgNode> &gen_node = *it;
			size_t genId = gen_node->GetId();
			cout << genId << ":";
			CTacAddr* gen_def = gen_node->GetDef();
			cout << gen_def;
			if (gen_node != *reach._gen.crbegin())
				cout << ",";
		}
		if (reach._gen.empty())
			cout << "NULL";
		cout << "\t| ";

		// print kill
		for (setCitCfgNode it = reach._kill.cbegin(); it != reach._kill.cend(); ++it) {
			const shared_ptr<CfgNode> &kill_node = *it;
			size_t killId = kill_node->GetId();
			cout << killId << ":";
			CTacAddr* kill_def = kill_node->GetDef();
			cout << kill_def;
			if (kill_node != *reach._kill.crbegin())
				cout << ",";
		}
		if (reach._kill.empty())
			cout << "NULL";
		cout << "\n";
	}
	cout << endl;
}

void CfgProc::DumpReach(const unsigned int step, const CfgProc *proc) const {
	cout << "Iteration : " << step << endl;
	cout << "NodeId\t| " << "preds\t| " << "gen\t| " << "kill\t| " << "in\t| "
			<< "out\n";
	const list<shared_ptr<CfgNode>> &nodes = proc->GetNodes();
	for (citCfgNode node_it = nodes.cbegin(); node_it != nodes.cend();
			++node_it) {
		const shared_ptr<CfgNode> &node = *node_it;
		//print node id
		size_t nodeId = node->GetId();
		cout << "n[" << nodeId << "]:\t| ";

		// print preds
		const list<shared_ptr<CfgNode>> &preds = node->GetPreds();
		for (citCfgNode it = preds.cbegin(); it != preds.cend(); ++it) {
			const shared_ptr<CfgNode> &pred = *it;
			size_t predId = pred->GetId();
			cout << predId;
			if (pred != preds.back())
				cout << ",";
		}
		if (preds.empty())
			cout << "NULL";
		cout << "\t| ";

		CfgNode::REACH &reach = node->GetReachInfo();
		// print gen
		for (setCitCfgNode it = reach._gen.cbegin(); it != reach._gen.cend(); ++it) {
			const shared_ptr<CfgNode> &gen_node = *it;
			size_t genId = gen_node->GetId();
			cout << genId << ":";
			CTacAddr* def = gen_node->GetDef();
			cout << def;
			if (gen_node != *reach._gen.crbegin())
				cout << ",";
		}
		if (reach._gen.empty())
			cout << "NULL";
		cout << "\t| ";

		// print kill
		for (setCitCfgNode it = reach._kill.cbegin(); it != reach._kill.cend(); ++it) {
			const shared_ptr<CfgNode> &kill_node = *it;
			size_t killId = kill_node->GetId();
			cout << killId << ":";
			CTacAddr* def = kill_node->GetDef();
			cout << def;
			if (kill_node != *reach._kill.crbegin())
				cout << ",";
		}
		if (reach._kill.empty())
			cout << "NULL";
		cout << "\t| ";

		// print liveIn
		for (setCitCfgNode it = reach._reachIn.cbegin();
				it != reach._reachIn.cend(); ++it) {
			const shared_ptr<CfgNode> &live_node = *it;
			size_t liveId = live_node->GetId();
			cout << liveId << ":";
			CTacAddr* def = live_node->GetDef();
			cout << def;
			if (live_node != *reach._reachIn.crbegin())
				cout << ",";
		}
		if (reach._reachIn.empty())
			cout << "NULL";
		cout << "\t| ";

		// print liveOut
		for (setCitCfgNode it = reach._reachOut.cbegin();
				it != reach._reachOut.cend(); ++it) {
			const shared_ptr<CfgNode> &live_node = *it;
			size_t liveId = live_node->GetId();
			cout << liveId << ":";
			CTacAddr* def = live_node->GetDef();
			cout << def;
			if (live_node != *reach._reachOut.crbegin())
				cout << ",";
		}
		if (reach._reachOut.empty())
			cout << "NULL";
		cout << "\n";
	}
	cout << endl;
}

void CfgProc::MakeNodes(void) {
	const list<CTacInstr*> &ops = _cb->GetInstr();
	for (citCTacInstr it = ops.cbegin(); it != ops.cend(); ++it) {
		CTacInstr *instr = *it;
		shared_ptr<CfgNode> n(new CfgNode(this, instr));
		_nodes.push_back(n);
	}
}

void CfgProc::MakeEdges(void) {
	citCfgNode it = _nodes.cbegin();
	while (it != _nodes.cend()) {
		const shared_ptr<CfgNode> &n = *it++;
		if (it != _nodes.cend()) {
			// get next node (fall through case)
			const shared_ptr<CfgNode> &next = *it;
			const CTacInstr *instr = n->GetInstr();
			// get dest instr (jump case)
			const CTacInstr *dest = dynamic_cast<const CTacInstr*>(instr->GetDest());
			if (!dest) {
				AddEdge(n, next);	// fall through
				continue;
			}
			// get dest node (jump case)
			const shared_ptr<CfgNode> &target = FindNode(dest);
			if (!target) {
				cout << "Node not found at instr_id : " << dest->GetId()
						<< endl;
				continue;
			}
			// "if true goto" or just "goto"
			AddEdge(n, target); 	// jump
			// "if false goto"
			if (IsRelOp(instr->GetOperation())) {
				AddEdge(n, next);	// fall through
			}
		}
	}
}

//------------------------------------------------------------------------------
// CfgIntraProc
//

CfgIntraProc::CfgIntraProc(CModule *m) {
	assert(m != NULL);
	if (!m)
		return;
	_m = m;
	_name = m->GetName();
	// initial CfgProc offset
	size_t offset = 0;
	CCodeBlock *cb = _m->GetCodeBlock();

	const vector<CSymbol*> &symbols = m->GetSymbolTable()->GetSymbols();
	vector<CSymbol*> globals;
	for (size_t s = 0; s < symbols.size(); ++s) {
		if (symbols[s]->GetSymbolType() == stGlobal){
			_globals.push_back(symbols[s]->GetName());
		}
	}

	// increment offset for next CfgProc
	offset += MakeProcs(cb, offset);
	const vector<CScope*> &proc = _m->GetSubscopes();
	for (size_t p = 0; p < proc.size(); ++p) {
		cb = proc[p]->GetCodeBlock();
		// increment offset for next CfgProc
		offset += MakeProcs(cb, offset);
	}
}

CfgIntraProc::~CfgIntraProc(void) {

}

const shared_ptr<CfgProc> CfgIntraProc::FindProc(const string &name) const {
	for (size_t p = 0; p < _procs.size(); ++p) {
		if (_procs[p]->GetName() == name)
			return _procs[p];
	}
	return nullptr;
}

void CfgIntraProc::toDot(ostream &out) const {
	for (size_t p = 0; p < _procs.size(); ++p) {
		_procs[p]->toDot(out);
	}
}

size_t CfgIntraProc::MakeProcs(CCodeBlock *cb, size_t offset) {
	shared_ptr<CfgProc> proc(new CfgProc(cb, offset, _globals));
	_procs.push_back(proc);
	return proc->GetNodeCnt();
}

//------------------------------------------------------------------------------
// CfgInterProc
//

CfgInterProc::CfgInterProc(CModule *m) :
		CfgIntraProc(m) {
	assert(m != NULL);
	if (!m)
		return;
	MakeGraph();
}

CfgInterProc::~CfgInterProc(void) {

}

void CfgInterProc::MakeGraph() {
	for (size_t p = 0; p < _procs.size(); ++p) {
		const list<shared_ptr<CfgNode>> &nodes = _procs[p]->GetNodes();
		list<shared_ptr<CfgNode>> node_range;
		for (citCfgNode it = nodes.cbegin(); it != nodes.cend(); ++it) {
			const shared_ptr<CfgNode> &node = *it;
			node_range.push_back(node);
			const CTacInstr *instr = node->GetInstr();
			EOperation op = instr->GetOperation();
			// make edges between procs for func calls
			if (op == opCall) {
				const CTacName *func =
						dynamic_cast<const CTacName*>(instr->GetSrc(1));
				if (!func) {
					cout << "Called function not found at instr_id : "
							<< instr->GetId() << endl;
					continue;
				}
				const string &name = func->GetSymbol()->GetName();
				const shared_ptr<CfgProc> &dest = FindProc(name);
				if (!dest) {
					list<string> io_funcs = { "WriteInt", "WriteStr",
							"WriteChar", "WriteLn", "ReadInt", "DIM", "DOFS" };
					if (!(find(io_funcs.begin(), io_funcs.end(), name)
							!= io_funcs.end())) {
						cout << "Function [" << name << "] not found in : "
								<< _name << ".mod" << endl;
					}
					continue;
				}
				const list<shared_ptr<CfgNode>> &target = dest->GetNodes();
				if (target.empty()) {
					cout << "Function [" << name << "] nodes not found" << endl;
					continue;
				}

				// edge from func call to func
				_procs[p]->AddEdge(node, target.front());
				// edge from func return to func call
				dest->AddEdge(target.back(), node);

				// global data-flow
				if (dest != _procs[p]){
					map<CTacAddr*, shared_ptr<CfgNode>, CTacAddrCmp> base_globals;
					BaseGlobals(node_range, base_globals);
					map<CTacAddr*, shared_ptr<CfgNode>, CTacAddrCmp> dest_globals;
					DestGlobals(dest, dest_globals);
					for (mapItCTacAddrCfgNode dit = dest_globals.begin();
							dit != dest_globals.end(); ++dit) {
						mapItCTacAddrCfgNode ret = base_globals.find(dit->first);
						if (ret != base_globals.end()) {
							cout << "Adding global dataflow edge: node["
									<< ret->second->GetId() << "] -> node["
									<< dit->second->GetId() << "] for "
									<< ret->first << endl;
							ret->second->GetGlobalInfo()._succs.insert(dit->second);
							dit->second->GetGlobalInfo()._preds.insert(ret->second);
						}
					}
				}
			}
		}
	}
}

void CfgInterProc::BaseGlobals(const list<shared_ptr<CfgNode>> &nodes,
		map<CTacAddr*, shared_ptr<CfgNode>, CTacAddrCmp> &globals) const {
	for (critCfgNode it = nodes.crbegin(); it != nodes.crend(); ++it) {
		const shared_ptr<CfgNode> &node = *it;
		CTacAddr *def = node->GetDef();
		if(!def)
			continue;

		if (node->VarIsGlobal(def)) {
			globals.insert(pair<CTacAddr*, shared_ptr<CfgNode>>(def, node));
		}

	}

	for (mapItCTacAddrCfgNode it = globals.begin(); it != globals.end();
			++it) {
		if (*it == *globals.begin()) {
			cout << "Found global variables in " << it->second->GetOwner()->GetName() << ":\n";
		}
		cout << "\t" << it->first << " in " << "node[" << it->second->GetId()
				<< "]";
		if (*it != *globals.rbegin()) {
			cout << ",\n";
		} else {
			cout << "\n" << endl;
		}
	}
}

void CfgInterProc::DestGlobals(const shared_ptr<CfgProc> &proc,
		map<CTacAddr*, shared_ptr<CfgNode>, CTacAddrCmp> &globals) const {
	const list<shared_ptr<CfgNode>> &nodes = proc->GetNodes();
	for (citCfgNode it = nodes.cbegin(); it != nodes.cend(); ++it) {
		const shared_ptr<CfgNode> &node = *it;
		const set<CTacAddr*, CTacAddrCmp> &global_vars = node->GetGlobal();
		if (!global_vars.empty()) {
			for (setCitCTacAddr git = global_vars.cbegin();
					git != global_vars.cend(); ++git) {
				globals.insert(pair<CTacAddr*, shared_ptr<CfgNode>>(*git, node));
			}
		}
	}

	for (mapItCTacAddrCfgNode it = globals.begin(); it != globals.end(); ++it) {
		if (*it == *globals.begin()) {
			cout << "Found global variables in " << proc->GetName() << ":\n";
		}
		cout << "\t" << it->first << " in " << "node[" << it->second->GetId()
				<< "]";
		if (*it != *globals.rbegin()) {
			cout << ",\n";
		} else {
			cout << "\n" << endl;
		}
	}
}
