

*表达式*
9 - 5 + 2
7
expr -> expr + term | expr - term | term
term -> term * factor | term / factor | factor
factor -> digit | ( expr )
digit -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

*EBNF形式 表达式*
expr ::= term { (+|-) term }*
term ::= factor { (*|/) factor }*
factor ::= ( expr )
    |   NUM


*函数调用*
optparams: 可选参数列表
null: 表示空

call      -> id ( optparams )
optparams -> params | null
parmas    -> params, param | param


*if for*
stmt -> expr;
    | if ( expr ) stmt
    | for (optexpr; optexpr; optexpr) stmt

optexpr -> null
    | expr


*二义性*
stmt -> id = expression
    | if ( expression ) stmt
    | if ( expression ) stmt
    | while ( expression ) stmt
    | { stmts }


stmts -> stmts stmt
    | null
