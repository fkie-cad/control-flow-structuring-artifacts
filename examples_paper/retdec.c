// RetDec version :  v5.0
// Commit hash    :  53e55b4b26e9b843787f0e06d867441e32b1604e
// Build date     :  2022-12-08T10:13:13Z

// Address range: 0x401136 - 0x401202
int64_t test_1(int64_t a1) {
    int64_t v1 = 0x100000000 * a1 >> 32; // 0x40113e
    printf("Block 1");
    int32_t v2 = v1;
    if ((int32_t)a1 > 6) {
        if (v2 == 125) {
            // 0x4011d0
            printf("Block 7");
            // 0x4011f0
            return printf("Block 9");
        }
        // 0x4011e1
        printf("Block 8");
        // 0x4011f0
        return printf("Block 9");
    }
    if (v2 < 2) {
        // 0x4011e1
        printf("Block 8");
        // 0x4011f0
        return printf("Block 9");
    }
    // 0x401166
    g3 = v1 & 0xffffffff;
    switch (v2) {
        case 2: {
            // 0x40117b
            printf("Block 2");
            // 0x4011f0
            return printf("Block 9");
        }
        case 3: {
            // 0x40118c
            printf("Block 3");
            // 0x4011f0
            return printf("Block 9");
        }
        case 4: {
            // 0x40119d
            printf("Block 4");
            // 0x4011f0
            return printf("Block 9");
        }
        case 5: {
            // 0x4011ae
            printf("Block 5");
            // 0x4011f0
            return printf("Block 9");
        }
        case 6: {
            // 0x4011bf
            printf("Block 6");
            // 0x4011f0
            return printf("Block 9");
        }
    }
    // 0x4011e1
    printf("Block 8");
    // 0x4011f0
    return printf("Block 9");
}



// Address range: 0x401202 - 0x401287
int64_t test_2(int64_t a1, int64_t a2) {
    // 0x401202
    printf("Block 1");
    if ((int32_t)a1 != 1) {
        // 0x401262
        printf("Block 2");
        printf("Block 4");
        // 0x401271
        printf("Block 6");
        return 0;
    }
    if ((int32_t)a2 != 1) {
        // 0x40124b
        printf("Block 2");
    } else {
        // 0x40124b
        printf("Block 3");
    }
    // 0x401251
    printf("Block 5");
    // 0x401271
    printf("Block 6");
    return 0;
}



// Address range: 0x401287 - 0x4012ff
int64_t test_3(int64_t a1, int64_t a2, int64_t a3) {
    // 0x401287
    printf("B1");
    if ((uint32_t)(int32_t)a2 >= 100) {
        // 0x4012ed
        return printf("B5");
    }
    printf("B2");
    // 0x4012a9
    while ((int32_t)a1 >= 20) {
        // 0x4012a9
        printf("B2");
    }
    // 0x4012ba
    printf("B3");
    if ((int32_t)a3 < 50) {
        // 0x4012ed
        return printf("B5");
    }
    while (true) {
        // 0x4012cf
        printf("B4");
        printf("B3");
    }
}



// Address range: 0x4012ff - 0x40139b
int64_t test_4(int64_t a1, int64_t a2) {
    // 0x4012ff
    printf("Block 1");
    int32_t v1 = a2;
    while (true) {
        lab_0x40136a_2:
        if ((int32_t)a1 == 1) {
            // 0x40131e
            printf("Block 3");
            if (v1 > 4) {
                // 0x401344
                printf("Block 5");
                if (v1 > 9) {
                    // 0x40135b
                    printf("Block 6");
                    goto lab_0x40136a_2;
                } else {
                    goto lab_0x40136a_2;
                }
            } else {
                // 0x401333
                printf("Block 4");
                // 0x40135b
                printf("Block 6");
                goto lab_0x40136a_2;
            }
        } else {
            // 0x401370
            printf("Block 2");
            if (v1 >= 20) {
                // break -> 0x401385
                break;
            }
            goto lab_0x40136a_2;
        }
    }
    // 0x401385
    printf("Block 7");
    return 0;
}
