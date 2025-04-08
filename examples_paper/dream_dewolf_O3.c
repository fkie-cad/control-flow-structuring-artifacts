// Binary Ninja Version 4.2.6455 - dewolf commit b42aa68 with the some modifications (see README.md) to better match the DREAM approach

long test_1(int arg1) {
    unsigned int var_17;
    printf(/* format */ "Block 1");
    if (arg1 == 125) {
        printf(/* format */ "Block 7");
        return printf(/* format */ "Block 9");
    }
    else if ((arg1 > 6) || (arg1 <= 1)) {
        printf(/* format */ "Block 8");
        return printf(/* format */ "Block 9");
    }
    if ((arg1 <= 6) && (arg1 > 1)) {
        var_17 = (unsigned int)(arg1 - 3);
        if (var_17 > 3) {
            printf(/* format */ "Block 2");
            return printf(/* format */ "Block 9");
        }
        else {
            switch(var_17) {
                case 0x0:
                    printf(/* format */ "Block 3");
                    return printf(/* format */ "Block 9");
                    break;
                case 0x1:
                    printf(/* format */ "Block 4");
                    return printf(/* format */ "Block 9");
                    break;
                case 0x2:
                    printf(/* format */ "Block 5");
                    return printf(/* format */ "Block 9");
                    break;
                case 0x3:
                    printf(/* format */ "Block 6");
                    return printf(/* format */ "Block 9");
                    break;
            }
        }
    }
}



long test_2(int arg1, int arg2) {
    printf(/* format */ "Block 1");
    if ((arg1 == 1) && (arg2 == 1)) {
        printf(/* format */ "Block 3");
    }
    else {
        printf(/* format */ "Block 2");
    }
    if (arg1 == 1) {
        printf(/* format */ "Block 5");
    }
    else {
        printf(/* format */ "Block 4");
    }
    printf(/* format */ "Block 6");
    return 0L;
}



long test_3(int arg1, int arg2, int arg3) {
    printf(/* format */ "B1");
    if (arg2 <= 99) {
        if (arg1 > 19) {
            while (true) {
                printf(/* format */ "B2");
                printf(/* format */ "B2");
            }
        }
        else {
            printf(/* format */ "B2");
            if (arg3 <= 49) {
                printf(/* format */ "B3");
            }
            else {
                while (true) {
                    printf(/* format */ "B3");
                    printf(/* format */ "B4");
                }
            }
        }
    }
    return printf(/* format */ "B5");
}



long test_4(int arg1, int arg2) {
    printf(/* format */ "Block 1");
    if (arg1 != 1) {
        if (arg2 > 19) {
            printf(/* format */ "Block 2");
            printf(/* format */ "Block 7");
            return 0L;
        }
        while (true) {
            printf(/* format */ "Block 2");
        }
    }
    else if (arg2 <= 4) {
        while (true) {
            printf(/* format */ "Block 3");
            printf(/* format */ "Block 4");
            printf(/* format */ "Block 6");
        }
    }
    else if (arg2 <= 9) {
        while (true) {
            printf(/* format */ "Block 3");
            printf(/* format */ "Block 5");
        }
    }
    else {
        while (true) {
            printf(/* format */ "Block 3");
            printf(/* format */ "Block 5");
            printf(/* format */ "Block 6");
        }
    }
}
