
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQVIrightIMPLIESleftANDORleftNOTleftFORALLEXISTSAND COMMA EQ EQVI EXISTS FORALL ID IMPLIES LPAREN NEQ NOT OR RPARENspec : spec : boolexpr specboolexpr : FORALL ID boolexprboolexpr : EXISTS ID boolexprboolexpr : boolexpr AND boolexpr\n                | boolexpr OR boolexpr\n                | boolexpr IMPLIES boolexpr\n                | boolexpr EQVI boolexprboolexpr : NOT boolexprboolexpr : term EQ termboolexpr : term NEQ termboolexpr : atomboolexpr : LPAREN boolexpr RPARENtermlist : term COMMA termlisttermlist : termterm : IDatom : ID LPAREN termlist RPAREN'
    
_lr_action_items = {'$end':([0,1,2,8,10,18,22,23,24,25,26,27,30,31,32,33,34,],[-1,0,-1,-12,-2,-9,-5,-6,-7,-8,-3,-16,-4,-10,-11,-13,-17,]),'FORALL':([0,2,6,8,9,11,12,13,14,15,17,18,22,23,24,25,26,27,30,31,32,33,34,],[3,3,3,-12,3,3,3,3,3,3,3,-9,-5,-6,-7,-8,-3,-16,-4,-10,-11,-13,-17,]),'EXISTS':([0,2,6,8,9,11,12,13,14,15,17,18,22,23,24,25,26,27,30,31,32,33,34,],[5,5,5,-12,5,5,5,5,5,5,5,-9,-5,-6,-7,-8,-3,-16,-4,-10,-11,-13,-17,]),'NOT':([0,2,6,8,9,11,12,13,14,15,17,18,22,23,24,25,26,27,30,31,32,33,34,],[6,6,6,-12,6,6,6,6,6,6,6,-9,-5,-6,-7,-8,-3,-16,-4,-10,-11,-13,-17,]),'LPAREN':([0,2,4,6,8,9,11,12,13,14,15,17,18,22,23,24,25,26,27,30,31,32,33,34,],[9,9,16,9,-12,9,9,9,9,9,9,9,-9,-5,-6,-7,-8,-3,-16,-4,-10,-11,-13,-17,]),'ID':([0,2,3,5,6,8,9,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,30,31,32,33,34,35,],[4,4,15,17,4,-12,4,4,4,4,4,4,27,4,-9,27,27,-5,-6,-7,-8,-3,-16,-4,-10,-11,-13,-17,27,]),'AND':([2,8,18,21,22,23,24,25,26,27,30,31,32,33,34,],[11,-12,-9,11,-5,-6,11,11,11,-16,11,-10,-11,-13,-17,]),'OR':([2,8,18,21,22,23,24,25,26,27,30,31,32,33,34,],[12,-12,-9,12,-5,-6,12,12,12,-16,12,-10,-11,-13,-17,]),'IMPLIES':([2,8,18,21,22,23,24,25,26,27,30,31,32,33,34,],[13,-12,-9,13,-5,-6,13,13,13,-16,13,-10,-11,-13,-17,]),'EQVI':([2,8,18,21,22,23,24,25,26,27,30,31,32,33,34,],[14,-12,-9,14,-5,-6,-7,14,14,-16,14,-10,-11,-13,-17,]),'EQ':([4,7,],[-16,19,]),'NEQ':([4,7,],[-16,20,]),'RPAREN':([8,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,],[-12,-9,33,-5,-6,-7,-8,-3,-16,34,-15,-4,-10,-11,-13,-17,-14,]),'COMMA':([27,29,],[-16,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'spec':([0,2,],[1,10,]),'boolexpr':([0,2,6,9,11,12,13,14,15,17,],[2,2,18,21,22,23,24,25,26,30,]),'term':([0,2,6,9,11,12,13,14,15,16,17,19,20,35,],[7,7,7,7,7,7,7,7,7,29,7,31,32,29,]),'atom':([0,2,6,9,11,12,13,14,15,17,],[8,8,8,8,8,8,8,8,8,8,]),'termlist':([16,35,],[28,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> spec","S'",1,None,None,None),
  ('spec -> <empty>','spec',0,'p_spec_0','prparse.py',141),
  ('spec -> boolexpr spec','spec',2,'p_spec','prparse.py',145),
  ('boolexpr -> FORALL ID boolexpr','boolexpr',3,'p_forall_quant','prparse.py',151),
  ('boolexpr -> EXISTS ID boolexpr','boolexpr',3,'p_exists_quant','prparse.py',155),
  ('boolexpr -> boolexpr AND boolexpr','boolexpr',3,'p_boolexpr_binop','prparse.py',159),
  ('boolexpr -> boolexpr OR boolexpr','boolexpr',3,'p_boolexpr_binop','prparse.py',160),
  ('boolexpr -> boolexpr IMPLIES boolexpr','boolexpr',3,'p_boolexpr_binop','prparse.py',161),
  ('boolexpr -> boolexpr EQVI boolexpr','boolexpr',3,'p_boolexpr_binop','prparse.py',162),
  ('boolexpr -> NOT boolexpr','boolexpr',2,'p_boolexpr_unop','prparse.py',176),
  ('boolexpr -> term EQ term','boolexpr',3,'p_boolexpr_eq','prparse.py',180),
  ('boolexpr -> term NEQ term','boolexpr',3,'p_boolexpr_neq','prparse.py',184),
  ('boolexpr -> atom','boolexpr',1,'p_boolexpr_atom','prparse.py',188),
  ('boolexpr -> LPAREN boolexpr RPAREN','boolexpr',3,'p_boolexpr_parentheses','prparse.py',200),
  ('termlist -> term COMMA termlist','termlist',3,'p_termlistN','prparse.py',206),
  ('termlist -> term','termlist',1,'p_termlist1','prparse.py',210),
  ('term -> ID','term',1,'p_term','prparse.py',214),
  ('atom -> ID LPAREN termlist RPAREN','atom',4,'p_atom','prparse.py',225),
]
