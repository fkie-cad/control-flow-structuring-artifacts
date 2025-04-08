// RetDec version :  v5.0
// Commit hash    :  53e55b4b26e9b843787f0e06d867441e32b1604e
// Build date     :  2022-12-08T10:13:13Z

// Address range: 0x401150 - 0x401261
int64_t test_1(int64_t a1) {
    // 0x401150
    printf("Block 1");
    int32_t v1 = a1; // 0x401162
    if (v1 > 6) {
        if (v1 == 125) {
            // 0x401189
            printf("Block 7");
            return printf("Block 9");
        }
        // 0x401228
        printf("Block 8");
        return printf("Block 9");
    }
    if (v1 < 2) {
        // 0x401228
        printf("Block 8");
        return printf("Block 9");
    }
    int64_t v2 = a1 + 0xfffffffd; // 0x40116d
    g3 = v2 & 0xffffffff;
    switch ((int32_t)v2) {
        case 0: {
            // 0x4011e8
            printf("Block 3");
            return printf("Block 9");
        }
        case 1: {
            // 0x401208
            printf("Block 4");
            return printf("Block 9");
        }
        case 2: {
            // 0x4011c8
            printf("Block 5");
            return printf("Block 9");
        }
        case 3: {
            // 0x4011a8
            printf("Block 6");
            return printf("Block 9");
        }
    }
    // 0x401248
    printf("Block 2");
    return printf("Block 9");
}



// Address range: 0x401270 - 0x4012df
int64_t test_2(int64_t a1, int64_t a2) {
    // 0x401270
    printf("Block 1");
    if ((int32_t)a1 != 1) {
        // 0x4012d1
        printf("Block 2");
        printf("Block 4");
        // 0x4012a8
        printf("Block 6");
        return 0;
    }
    if ((int32_t)a2 != 1) {
        // 0x4012c0
        printf("Block 2");
    } else {
        // 0x401290
        printf("Block 3");
    }
    // 0x40129c
    printf("Block 5");
    // 0x4012a8
    printf("Block 6");
    return 0;
}



// Address range: 0x4012e0 - 0x401376
int64_t test_3(int64_t a1, int64_t a2, int64_t a3) {
    // 0x4012e0
    printf("B1");
    if ((int32_t)a2 > 99) {
        // 0x401366
        return printf("B5");
    }
    if ((uint32_t)(int32_t)a1 >= 20) {
        while (true) {
            // 0x401302
            printf("B2");
            printf("B2");
        }
    }
    // 0x401320
    printf("B2");
    if ((int32_t)a3 < 50) {
        // 0x40135a
        printf("B3");
        // 0x401366
        return printf("B5");
    }
    while (true) {
        // 0x401340
        printf("B3");
        printf("B4");
    }
}



// Address range: 0x401380 - 0x40145a
int64_t test_4(int64_t a1, int64_t a2) {
    // 0x401380
    printf("Block 1");
    int32_t v1 = a2;
    if ((int32_t)a1 != 1) {
        if (v1 > 19) {
            // 0x4013ae
            printf("Block 2");
            printf("Block 7");
            return 0;
        }
        while (true) {
            // 0x4013a0
            printf("Block 2");
        }
    }
    if (v1 < 5) {
        while (true) {
            // 0x401410
            printf("Block 3");
            printf("Block 4");
            printf("Block 6");
        }
    }
    if (v1 < 10) {
        while (true) {
            // 0x401440
            printf("Block 3");
            printf("Block 5");
        }
    }
    while (true) {
        // 0x4013e0
        printf("Block 3");
        printf("Block 5");
        printf("Block 6");
    }
}
