grammar am;

program: prog;

prog: statement (statement)*;

statement: 
        simple
        | complexStatement
        ;

simple: 
        fetch
        | push
        | store
        | simple_commands
        ;

simple_commands: 
       'ADD'
       | 'MULT'
       | 'SUB'
       | 'DIV'
       | 'TRUE'
       | 'FALSE'
       | 'EQ'
       | 'LE'
       | 'AND'
       | 'OR'
       | 'NEG'
       | 'NOOP'
       ;

fetch: 'FETCH(' VARIABLE ')';

push: 'PUSH(' NUMBER ')';

store:  'STORE(' VARIABLE ')';

complexStatement: branch | loop;

branch: 'BRANCH(' prog ',' prog ')';

loop: 'LOOP(' prog ',' prog ')';

VARIABLE: [a-zA-Z]+ ;
NUMBER: [0-9]+ ;

WS: [ \t\r\n]+ -> skip;
