//
//  main.c
//  2.1.3
//
//  Created by working on 2018/5/2.
//  Copyright © 2018年 working. All rights reserved.
//
#if 1

#include <stdio.h>

typedef unsigned char *byte_pointer;

void
show_bytes(byte_pointer start, size_t len) {
    size_t i;
    for (i = 0; i < len; i++) {
        printf("%.2x ", start[i]);
    }
    printf("\n");
}

void
show_int(int x) {
    show_bytes((byte_pointer)&x, sizeof(int));
}

void
show_float(float x) {
    show_bytes((byte_pointer)&x, sizeof(float));
}

void
show_pointer(void *x) {
    show_bytes((byte_pointer)&x, sizeof(void *));
}

/*
 39 30 00 00
 00 e4 40 46
 f8 f5 bf ef fe 7f 00 00 
 */
void
test_show_bytes(int val) {
    int ival = val;
    float fval = (float)ival;
    int *pval = &ival;
    
    show_int(ival);
    show_float(fval);
    show_pointer(pval);
}

void
test_2_5() {
    int val = 0x87654321;
    byte_pointer valp = (byte_pointer)&val;
    show_bytes(valp, 1);
    show_bytes(valp, 2);
    show_bytes(valp, 3);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    test_2_5();
    return 0;
}

#endif
