//
//  common.cpp
//  scope
//
//  Created by working on 2018/9/1.
//  Copyright © 2018年 working. All rights reserved.
//

#include "common.hpp"

using namespace std;

/**
 返回代码下一个字符
 @param src src 代码源码
 @param currentIndex 当前下标
 @return 下一个字符
 */
string NextChar(string src, int currentIndex) {
    size_t l = src.length();
    int index = currentIndex;
    assert(index < l);
    
    int n = 1;
    string s(&src.at(index), n);
    return s;
}
