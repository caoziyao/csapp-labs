//
//  main.cpp
//  nasm
//
//  Created by working on 2018/9/25.
//  Copyright © 2018年 working. All rights reserved.
//

#include <iostream>
#include <stdio.h>

extern "C" long long GetRDTSC();

int main(int, const char**)
{
    long long RDTSC1 = GetRDTSC();
    
    printf("res: %lld \n", RDTSC1);
    
//    long long RDTSC2 = GetRDTSC();
//    printf("Time-Stamp Counters: %lld - %lld\n", RDTSC1, RDTSC2);
    return 0;
}
