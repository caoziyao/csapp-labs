//
//  TestCommon.cpp
//  scope
//
//  Created by working on 2018/9/1.
//  Copyright © 2018年 working. All rights reserved.
//

#include "TestCommon.hpp"

using namespace std;

TEST(NextChar, Positive) {
    // todo
//    map<string, string> data;

    string path = "/Users/Shared/github/csapp-labs/scope/m.txt";
    
    cout << "path lenght: " << path.length() << endl;
    string s = NextChar(path, 2);
    
     cout << "s lenght: " << s.length() << endl;
    cout << "ddd: " << NextChar(path, 2) << endl;
//    EXPECT_EQ("p", NextChar(path, 0));
//
//    cout << s << endl;
    //    EXPECT_EQ(2, Foo(4, 10));
    //    EXPECT_EQ(6, Foo(30, 18));
}

