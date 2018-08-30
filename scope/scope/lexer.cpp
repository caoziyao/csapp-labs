////
////  lexer.cpp
////  scope
////
////  Created by working on 2018/8/30.
////  Copyright © 2018年 working. All rights reserved.
////
//
//#include "lexer.hpp"
//#include "ExprAST.hpp"
//using namespace std;
//
//static string IdentifierStr;  // Filled in if tok_identifier
//static double NumVal;         // Filled in if tok_number
//
//static int CurTok;
//static int getNextToken() {
//    return CurTok = gettok();
//}
//
///// Error* - These are little helper functions for error handling.
//ExprAST *Error(const char *Str) { fprintf(stderr, "Error: %s\n", Str);return 0;}
//PrototypeAST *ErrorP(const char *Str) { Error(Str); return 0; }
//FunctionAST *ErrorF(const char *Str) { Error(Str); return 0; }
//
//
//enum Token {
//    tok_eof = -1,
//    
//    // commands
//    tok_def = -2,
//    tok_extern = -3,
//    
//    // primary
//    tok_identifier = -4,
//    tok_number = -5,
//};
//
//// static 词法分析
// int gettok() {
//    static int LastChar = ' ';
//    
//    // ship any whiteespace
//    while (isspace(LastChar)) {
//        LastChar = getchar();
//    }
//    
//    // identifier: [a-zA-Z][a-zA-Z0-9]*
//    if (isalpha(LastChar)) {
//        IdentifierStr = LastChar;
//        
//        while (isalnum(LastChar = getchar())) {
//            IdentifierStr += LastChar;
//        }
//        
//        // def extern
//        if (IdentifierStr == "def") {
//            return tok_def;
//        }
//        else if (IdentifierStr == "extern") {
//            return tok_extern;
//        }
//        return tok_identifier;
//    }
//    
//    // Number: [0-9.]+
//    if (isdigit(LastChar) || LastChar == '.') {
//        string NumStr;
//        do {
//            NumStr += LastChar;
//            LastChar = getchar();
//        } while (isdigit(LastChar) || LastChar == '.');
//        // NumVal = strtod(NumStr.c_str());
//        NumVal = atoi(NumStr.c_str());
//        return tok_number;
//    }
//    
//    // Comment until end of line.
//    if (LastChar == '#') {
//        do {
//            LastChar = getchar();
//        }while (LastChar != EOF && LastChar != '\n' && LastChar != '\r');
//        
//        if (LastChar != EOF)
//            return gettok();
//    }
//    
//    // Check for end of file.  Don't eat the EOF.
//    if (LastChar == EOF)
//        return tok_eof;
//    
//    // Otherwise, just return the character as its ascii value.
//    int ThisChar = LastChar;
//    LastChar = getchar();
//    return ThisChar;
//}
//
//// static ExprAST
///// numberexpr ::= number
//ExprAST *ParseNumberExpr() {
//    ExprAST *r = new NumberExprAST(NumVal);
//    getNextToken();
//    return r;
//}
//
///// static parenexpr ::= '(' expression ')'
// ExprAST *ParseParenExpr() {
//    getNextToken();  // eat (.
//    ExprAST *V = ParseExpression();
//    if (!V) return 0;
//    
//    if (CurTok != ')')
//        return Error("expected ')'");
//    getNextToken();  // eat ).
//    return V;
//}
//
