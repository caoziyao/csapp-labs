//
//  Lexer.hpp
//  scope
//
//  Created by working on 2018/8/31.
//  Copyright © 2018年 working. All rights reserved.
//

#ifndef Lexer_hpp
#define Lexer_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <cassert>
#include "patch.hpp"
#include "FileManger.hpp"
#include "common.hpp"

static std::string IdentifierStr; // Filled in if tok_identifier
static double NumVal;             // Filled in if tok_number

enum Token {
    tok_eof = -1,
    
    // commands
    tok_def = -2,
    tok_extern = -3,
    
    // primary
    tok_identifier = -4,
    tok_number = -5,
};

/// gettok - Return the next token from standard input.
int gettok();

#endif /* Lexer_hpp */
