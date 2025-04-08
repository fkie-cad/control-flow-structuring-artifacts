// Angr Version - sailr-eval commit f5a30c3a0312a669e9f6f87acab7473618dd97cf

// Python script: (angr_dec file from sailr_eval)
// from angr_dec import angr_decompile
// print(angr_decompile("example_samples", functions=None, print_dec=True, dump_early_metrics= False, dump_line_maps= False))


long long test_1(unsigned long a0) {
    printf("Block 1");
    if (a0 <= 6) {
        switch (a0) {
            case 2:
                printf("Block 2");
                return printf("Block 9");
            case 3:
                printf("Block 3");
                return printf("Block 9");
            case 4:
                printf("Block 4");
                return printf("Block 9");
            case 5:
                printf("Block 5");
                return printf("Block 9");
            case 6:
                printf("Block 6");
                return printf("Block 9");
            default:
                printf("Block 8");
        }
        return printf("Block 9");
    } else if (a0 != 125) {
        printf("Block 8");
    } else {
        printf("Block 7");
        return printf("Block 9");
    }
}



long long test_2(unsigned long a0, unsigned long a1) {
    printf("Block 1");
    if (a0 != 1 || a1 != 1)
        printf("Block 2");
    else
        printf("Block 3");
    if (a0 != 1)
        printf("Block 4");
    else
        printf("Block 5");
    printf("Block 6");
    return 0;
}



long long test_3(unsigned long a0, unsigned long a1, unsigned long a2) {
    printf("B1");
    while (a1 <= 99) {
        printf("B2");
        while (a0 <= 19) {
            printf("B3");
            if (a2 <= 49)
                return printf("B5");
            printf("B4");
        }
    }
    return printf("B5");
}



long long test_4(unsigned long a0, unsigned long a1) {
    printf("Block 1");
    while (true) {
        if (a0 != 1) {
            printf("Block 2");
            if (a1 > 19)
                break;
        } else {
            printf("Block 3");
            if (a1 <= 4) {
                printf("Block 4");
            } else {
                printf("Block 5");
                if (a1 <= 9)
                    continue;
            }
            printf("Block 6");
        }
    }
    printf("Block 7");
    return 0;
}


