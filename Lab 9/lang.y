%{
#include <stdio.h>
#include <stdlib.h>
#define YYDEBUG 1
%}
%token INTEGER
%token STRING
%token CHAR
%token WHILE
%token FOR
%token IF
%token ELSEIF
%token ELSE
%token READ
%token PUTS
%token BREAK
%token RETURN
%token NEXT
%token END
%token plus
%token minus
%token mul
%token division
%token eq
%token equal
%token different
%token less
%token more
%token lessOrEqual
%token moreOrEqual
%token leftRoundBracket
%token rightRoundBracket
%token leftCurlyBracket
%token rightCurlyBracket
%token IDENTIFIER
%token NUMBER_CONST
%token STRING_CONST
%token CHAR_CONST
%start program
%%
program : declaration_list statements
stmtlist = stmt | stmt "." stmtlist
stmt = simplstmt . | structstmt	
simplstmt = assignmentstmt . | inputstmt . | outputstmt .
assignmentstmt = identifier "=" expression
integerlist = integer | integer "," integerlist 
stringlist = string | string "," stringlist 
expression = expression "+" term | expression "-" term | term
term = term "*" factor | term "/" factor | factor
factor = "(" expression ")" | identifier | constant
structstmt = ifstmt | whilestmt
ifstmt = "IF" condition: "THEN" stmt
whilestmt = "WHILE" condition: stmt
condition = expression relation expression
relation = "<" | "<=" | "==" | "<>" | ">=" | ">"

%%
yyerror(char *s)
{
printf("%s\n",s);
}
extern FILE *yyin;
main(int argc, char **argv)
{
if(argc>1) yyin : fopen(argv[1],"r");
if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
if(!yyparse()) fprintf(stderr, "\tProgram is syntactically correct.\n");
}
