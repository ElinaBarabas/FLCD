
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     INTEGER = 258,
     STRING = 259,
     CHAR = 260,
     WHILE = 261,
     FOR = 262,
     IF = 263,
     ELSEIF = 264,
     ELSE = 265,
     READ = 266,
     PUTS = 267,
     BREAK = 268,
     RETURN = 269,
     NEXT = 270,
     END = 271,
     plus = 272,
     minus = 273,
     mul = 274,
     division = 275,
     eq = 276,
     equal = 277,
     different = 278,
     less = 279,
     more = 280,
     lessOrEqual = 281,
     moreOrEqual = 282,
     leftRoundBracket = 283,
     rightRoundBracket = 284,
     leftCurlyBracket = 285,
     rightCurlyBracket = 286,
     IDENTIFIER = 287,
     NUMBER_CONST = 288,
     STRING_CONST = 289,
     CHAR_CONST = 290
   };
#endif
/* Tokens.  */
#define INTEGER 258
#define STRING 259
#define CHAR 260
#define WHILE 261
#define FOR 262
#define IF 263
#define ELSEIF 264
#define ELSE 265
#define READ 266
#define PUTS 267
#define BREAK 268
#define RETURN 269
#define NEXT 270
#define END 271
#define plus 272
#define minus 273
#define mul 274
#define division 275
#define eq 276
#define equal 277
#define different 278
#define less 279
#define more 280
#define lessOrEqual 281
#define moreOrEqual 282
#define leftRoundBracket 283
#define rightRoundBracket 284
#define leftCurlyBracket 285
#define rightCurlyBracket 286
#define IDENTIFIER 287
#define NUMBER_CONST 288
#define STRING_CONST 289
#define CHAR_CONST 290




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


