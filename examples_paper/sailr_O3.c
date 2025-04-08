// Angr Version - sailr-eval commit f5a30c3a0312a669e9f6f87acab7473618dd97cf

// Python script: (angr_dec file from sailr_eval)
// from angr_dec import angr_decompile
// print(angr_decompile("example_samples_O3", functions=None, print_dec=True, dump_early_metrics= False, dump_line_maps= False))


long long test_1(unsigned long a0) {
    printf("Block 1");
    switch (a0) {
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
            printf("Block 2");
            return printf("Block 9");
    }
    printf("Block 8");
    return printf("Block 9");
}



long long test_2(unsigned long a0, unsigned long a1) {
    printf("Block 1");
    if (a0 == 1 && a1 == 1) {
        printf("Block 3");
        printf("Block 5");
    }
    printf("Block 2");
    if (a0 == 1)
        printf("Block 5");
    else
        printf("Block 4");
    printf("Block 6");
    return 0;
}



long long test_3(unsigned long a0, unsigned long a1, unsigned long a2) {
    printf("B1");
    if (a1 > 99)
        return printf("B5");
    if (a0 <= 19) {
        printf("B2");
        if (a2 <= 49) {
            printf("B3");
            return printf("B5");
        }
        while (true) {
            printf("B3");
            printf("B4");
        }
    } else {
        while (true) {
            printf("B2");
            printf("B2");
        }
    }
}



long long test_4(unsigned long a0, unsigned long a1) {
    printf("Block 1");
    if (a0 != 1) {
        if (a1 > 19) {
            printf("Block 2");
            printf("Block 7");
            return 0;
        }
        while (true) {
            printf("Block 2");
        }
    } else if (a1 <= 4) {
        while (true) {
            printf("Block 3");
            printf("Block 4");
            printf("Block 6");
        }
    } else if (a1 > 9) {
        while (true) {
            printf("Block 3");
            printf("Block 5");
            printf("Block 6");
        }
    } else {
        while (true) {
            printf("Block 3");
            printf("Block 5");
        }
    }
}
