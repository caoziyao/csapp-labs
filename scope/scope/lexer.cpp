//
//  Lexer.cpp
//  scope
//
//  Created by working on 2018/8/31.
//  Copyright © 2018年 working. All rights reserved.
//

#include "Lexer.hpp"


using namespace std;



int gettok() {
    static int LastChar = ' ';
    string path = "/Users/Shared/github/csapp-labs/scope/m.txt";
    string src = Read(path);
    
    cout << "src: " + src << endl;
    
    // Skip any whitespace.
//    while (isspace(LastChar)) {
//        LastChar = getchar();
//        cout << "lastcahr: " << LastChar << endl;
//    }
//
//    if (isalpha(LastChar)) {
//        IdentifierStr = LastChar;
//        while (isalnum(LastChar == getchar())) {
//            IdentifierStr += LastChar;
//        }
//
//        cout << "IdentifierStr: " << IdentifierStr << endl;
//    }

    return 0;
}
