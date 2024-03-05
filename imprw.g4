grammar imprw;

progr: series;

series: stmt ';'  | series ';' stmt;

stmt: inputStmt
    | outputStmt
    | assignStmt
    | condStmt
    | loop
    | stmt ';' stmt
    | 'skip';

inputStmt: 'read' varlist;

outputStmt: 'write' varlist;

assignStmt: VARNAME ':=' expr;

condStmt: 'if' compar 'then' series ('else' series)? 'fi';

loop: 'while' compar 'do' series 'od';

compar: comparterm | compar 'or' comparterm;

comparterm: comparelem | comparterm 'and' comparelem;

comparelem: expr RELATION expr | expr | 'not' compar;

varlist: VARNAME (',' VARNAME)*;

expr: term | expr WEAKOP term;

term: negelem | term STRONGOP negelem;

negelem: elem; 

elem: VARNAME | NUMBER | TRUTHVAL | '(' expr ')';

NUMBER: [1-9][0-9]*;

VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;

RELATION: '=' | '<>' | '<' | '>' | '<=' | '>=';

WEAKOP: '+' | '-';

STRONGOP: '*' | '/';

TRUTHVAL: 'true' | 'false';

WS: [ \t\r\n]+ -> skip;
