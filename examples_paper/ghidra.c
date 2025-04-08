// Ghidra Version 11.3.1

void test_1(int param_1)

{
    printf("Block 1");
    if (param_1 < 7) {
        switch(param_1) {
            case 2:
                printf("Block 2");
                break;
            case 3:
                printf("Block 3");
                break;
            case 4:
                printf("Block 4");
                break;
            case 5:
                printf("Block 5");
                break;
            case 6:
                printf("Block 6");
                break;
            default:
                goto switchD_00401171_caseD_5;
        }
    }
    else {
        if (param_1 == 0x7d) {
            printf("Block 7");
            goto LAB_004011f0;
        }
        switchD_00401171_caseD_5:
            printf("Block 8");
    }
    LAB_004011f0:
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
    }
    if (param_1 == 1) {
        printf("Block 5");
    }
    else {
        printf("Block 4");
    }
    printf("Block 6");
    return 0;
}



void test_3(int param_1,int param_2,int param_3)

{
    printf("B1");
    while (param_2 < 100) {
        printf("B2");
        while (param_1 < 0x14) {
            printf("B3");
            if (param_3 < 0x32) goto LAB_004012ed;
            printf("B4");
        }
    }
    LAB_004012ed:
    printf("B5");
    return;
}



undefined8 test_4(int param_1,int param_2)

{
    printf("Block 1");
    LAB_0040136a:
    while (param_1 != 1) {
        printf("Block 2");
        if (0x13 < param_2) {
            printf("Block 7");
            return 0;
        }
    }
    printf("Block 3");
    if (4 < param_2) goto LAB_00401344;
    printf("Block 4");
    goto LAB_0040135b;
    LAB_00401344:
    printf("Block 5");
    if (9 < param_2) {
        LAB_0040135b:
        printf("Block 6");
    }
    goto LAB_0040136a;
}
