////
////  ExprAST.hpp
////  scope
////
////  Created by working on 2018/8/30.
////  Copyright © 2018年 working. All rights reserved.
////
//
//#ifndef ExprAST_hpp
//#define ExprAST_hpp
//
//#include <stdio.h>
//#include <iostream>
//#include <vector>
//
//class ExprAST {
//public:
//    virtual ~ExprAST() {}
//};
//
//
///// NumberExprAST - Expression class for numeric literals like "1.0".
//class NumberExprAST : public ExprAST {
//    double Val;
//public:
//    NumberExprAST(double val) : Val(val) {}
//};
//
//
///// VariableExprAST - Expression class for referencing a variable, like "a".
//// VariableExprAST用于保存变量名
//class VariableExprAST : public ExprAST {
//    std::string Name;
//public:
//    VariableExprAST(const std::string &name) : Name(name) {}
//};
//
//
///// BinaryExprAST - Expression class for a binary operator.
//// BinaryExprAST用于保存运算符（如“+”）
//class BinaryExprAST : public ExprAST {
//    char Op;
//    ExprAST *LHS, *RHS;
//public:
//    BinaryExprAST(char op, ExprAST *lhs, ExprAST *rhs)
//    : Op(op), LHS(lhs), RHS(rhs) {}
//};
//
//
///// CallExprAST - Expression class for function calls.
////CallExprAST用于保存函数名和用作参数的表达式列表
//class CallExprAST : public ExprAST {
//    std::string Callee;
//    std::vector<ExprAST*> Args;
//public:
//    CallExprAST(const std::string &callee, std::vector<ExprAST*> &args)
//    : Callee(callee), Args(args) {}
//};
//
//
//// 函数的接口和函数本身
///// PrototypeAST - This class represents the "prototype" for a function,
///// which captures its name, and its argument names (thus implicitly the number
///// of arguments the function takes).
//class PrototypeAST {
//    std::string Name;
//    std::vector<std::string> Args;
//public:
//    PrototypeAST(const std::string &name, const std::vector<std::string> &args)
//    : Name(name), Args(args) {}
//    
//};
//
///// FunctionAST - This class represents a function definition itself.
//class FunctionAST {
//    PrototypeAST *Proto;
//    ExprAST *Body;
//public:
//    FunctionAST(PrototypeAST *proto, ExprAST *body)
//    : Proto(proto), Body(body) {}
//    
//};
//
//
//#endif /* ExprAST_hpp */

