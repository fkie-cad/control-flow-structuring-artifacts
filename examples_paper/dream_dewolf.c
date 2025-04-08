// Binary Ninja Version 4.2.6455 - dewolf commit b42aa68 with the some modifications (see README.md) to better match the DREAM approach


long test_1(int arg1) {
    long var_20;
    printf(/* format */ "Block 1");
    if (arg1 == 125) {
        printf(/* format */ "Block 7");
    }
    if (arg1 != 125) {
        switch(arg1) {
            case 0x2:
                printf(/* format */ "Block 2");
                break;
            case 0x3:
                printf(/* format */ "Block 3");
                break;
            case 0x4:
                printf(/* format */ "Block 4");
                break;
            case 0x5:
                printf(/* format */ "Block 5");
                break;
            case 0x6:
                printf(/* format */ "Block 6");
                break;
            default:
                printf(/* format */ "Block 8");
        }
    }
    var_20 = printf(/* format */ "Block 9");
    return var_20;
}



long test_2(int arg1, int arg2) {
    printf(/* format */ "Block 1");
    if ((arg1 == 1) && (arg2 == 1)) {
        printf(/* format */ "Block 3");
    }
    else {
        printf(/* format */ "Block 2");
    }
    if (arg1 != 1) {
        printf(/* format */ "Block 4");
    }
    else {
        printf(/* format */ "Block 5");
    }
    printf(/* format */ "Block 6");
    return 0L;
}



long test_3(int arg1, int arg2, int arg3) {
    int exit_4;
    long var_10;
    printf(/* format */ "B1");
    while (arg2 <= 99) {
        printf(/* format */ "B2");
        while (true) {
            if (arg1 > 19) {
                exit_4 = 0;
                break;
            }
            printf(/* format */ "B3");
            if (arg3 <= 49) {
                exit_4 = 1;
                break;
            }
            printf(/* format */ "B4");
        }
        if (exit_4 != 0) {
            break;
        }
    }
    var_10 = printf(/* format */ "B5");
    return var_10;
}



long test_4(int arg1, int arg2) {
    printf(/* format */ "Block 1");
    do {
        while (arg1 == 1) {
            printf(/* format */ "Block 3");
            if (arg2 > 4) {
                printf(/* format */ "Block 5");
            }
            else {
                printf(/* format */ "Block 4");
            }
            if ((arg2 > 4) && (arg2 <= 9)) {
                continue;
            }
            printf(/* format */ "Block 6");
        }
        printf(/* format */ "Block 2");
    }
    while (arg2 <= 19);
    printf(/* format */ "Block 7");
    return 0L;
}
