//
//  main.cpp
//  scope
//
//  Created by working on 2018/8/30.
//  Copyright © 2018年 working. All rights reserved.
//

/*
 # Compute the x'th fibonacci number.
 def fib(x)
 if x < 3 then
    1
 else
    fib(x-1)+fib(x-2)

 # This expression will compute the 40th number.
 fib(40)

 extern sin(arg);
 extern cos(arg);
 extern atan2(arg1 arg2);

 atan2(sin(.4), cos(42))
 */

#include <iostream>
#include "gtest/gtest.h"
#include "Lexer.hpp"

// Runs all tests using Google Test.
int RunTest(int argc,  char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

int main(int argc,  char ** argv) {
    RunTest(argc, argv);
    
    gettok();
    
    return 0;
}
