// Ghidra Version 11.3.1

void test_1(int param_1)

{
    printf("Block 1");
    if (param_1 < 7) {
        if (1 < param_1) {
            switch(param_1) {
                case 3:
                    printf("Block 3");
                    printf("Block 9");
                    return;
                case 4:
                    printf("Block 4");
                    printf("Block 9");
                    return;
                case 5:
                    printf("Block 5");
                    printf("Block 9");
                    return;
                case 6:
                    printf("Block 6");
                    printf("Block 9");
                    return;
                default:
                    printf("Block 2");
                    printf("Block 9");
                    return;
            }
        }
    }
    else if (param_1 == 0x7d) {
        printf("Block 7");
        printf("Block 9");
        return;
    }
    printf("Block 8");
    printf("Block 9");
    return;
}



undefined8 test_2(int param_1,int param_2)

{
    printf("Block 1");
    if ((param_1 == 1) && (param_2 == 1)) {
        printf("Block 3");
    }
    else {
        printf("Block 2");
        if (param_1 != 1) {
            printf("Block 4");
            goto LAB_004012a8;
        }
    }
    printf("Block 5");
    LAB_004012a8:
    printf("Block 6");
    return 0;
}



void test_3(int param_1,int param_2,int param_3)

{
    printf("B1");
    if (param_2 < 100) {
        if (0x13 < param_1) {
            do {
                printf("B2");
                printf("B2");
            } while( true );
        }
        printf("B2");
        if (0x31 < param_3) {
            do {
                printf("B3");
                printf("B4");
            } while( true );
        }
        printf("B3");
    }
    printf("B5");
    return;
}



undefined8 test_4(int param_1,int param_2)

{
    printf("Block 1");
    if (param_1 != 1) {
        if (0x13 < param_2) {
            printf("Block 2");
            printf("Block 7");
            return 0;
        }
        do {
            printf("Block 2");
        } while( true );
    }
    if (4 < param_2) {
        if (param_2 < 10) {
            do {
                printf("Block 3");
                printf("Block 5");
            } while( true );
        }
        do {
            printf("Block 3");
            printf("Block 5");
            printf("Block 6");
        } while( true );
    }
    do {
        printf("Block 3");
        printf("Block 4");
        printf("Block 6");
    } while( true );
}
