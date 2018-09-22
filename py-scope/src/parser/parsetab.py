
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE DOUBLE_EQUAL ELSE EQUAL FALSE ID IF LPAREN MINUS NUMBER PLUS RPAREN THEN TIMES TRUE VAR WHILEexpression : expression PLUS termexpression : id EQUAL valueexpression : expression MINUS termid : IDexpression : termvalue : NUMBERterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBER\n    factor : LPAREN expression RPAREN'
    
_lr_action_items = {'ID':([0,7,],[4,4,]),'NUMBER':([0,7,8,9,10,11,12,],[6,6,6,6,6,6,19,]),'LPAREN':([0,7,8,9,10,11,],[7,7,7,7,7,7,]),'$end':([1,2,5,6,14,15,16,17,18,19,20,],[0,-5,-9,-10,-1,-3,-7,-8,-2,-6,-11,]),'PLUS':([1,2,5,6,13,14,15,16,17,18,19,20,],[8,-5,-9,-10,8,-1,-3,-7,-8,-2,-6,-11,]),'MINUS':([1,2,5,6,13,14,15,16,17,18,19,20,],[9,-5,-9,-10,9,-1,-3,-7,-8,-2,-6,-11,]),'RPAREN':([2,5,6,13,14,15,16,17,18,19,20,],[-5,-9,-10,20,-1,-3,-7,-8,-2,-6,-11,]),'TIMES':([2,5,6,14,15,16,17,20,],[10,-9,-10,10,10,-7,-8,-11,]),'DIVIDE':([2,5,6,14,15,16,17,20,],[11,-9,-10,11,11,-7,-8,-11,]),'EQUAL':([3,4,],[12,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,7,],[1,13,]),'term':([0,7,8,9,],[2,2,14,15,]),'id':([0,7,],[3,3,]),'factor':([0,7,8,9,10,11,],[5,5,5,5,16,17,]),'value':([12,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parse_calculation.py',15),
  ('expression -> id EQUAL value','expression',3,'p_assignment','parse_assignment.py',17),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parse_calculation.py',20),
  ('id -> ID','id',1,'p_assignment_id','parse_assignment.py',23),
  ('expression -> term','expression',1,'p_expression_term','parse_calculation.py',25),
  ('value -> NUMBER','value',1,'p_assignment_value','parse_assignment.py',28),
  ('term -> term TIMES factor','term',3,'p_term_times','parse_calculation.py',30),
  ('term -> term DIVIDE factor','term',3,'p_term_div','parse_calculation.py',36),
  ('term -> factor','term',1,'p_term_factor','parse_calculation.py',41),
  ('factor -> NUMBER','factor',1,'p_factor_num','parse_calculation.py',46),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parse_calculation.py',53),
]
