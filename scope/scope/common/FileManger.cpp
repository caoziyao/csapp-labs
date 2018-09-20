//
//  FileManger.cpp
//  scope
//
//  Created by working on 2018/8/31.
//  Copyright © 2018年 working. All rights reserved.
//

#include "FileManger.hpp"

using namespace std;

//输出空行
void OutPutAnEmptyLine() {
    cout << '\n';
}

string Read(string path) {
    ifstream in(path.c_str());
    string s;
    string content;
    
    if (in) {
        while (getline(in, s)) {
            content += s;
        }
        in.close();
        return content;
    } else {
         cout << "open " +  path + " error!!!" << endl;
        return "error";
    }
}
