// Version r2-5.9.9 and r2pm-5.9.9 and r2dec 40899cd960ae198ebf841ddf410014fddd1ed831

int64_t test_1 (signed int64_t arg1) {
    signed int64_t var_4h;
    rdi = arg1;
    *((rbp - 4)) = edi;
    eax = 0;
    printf ("Block 1");
    if (*((rbp - 4)) <= 6) {
        if (*((rbp - 4)) < 2) {
            goto label_0;
        }
        if (*((rbp - 4)) > 6) {
            goto label_0;
        }
        eax = *((rbp - 4));
        rax = *((rax*8 + 0x402050));
        /* switch table (7 cases) at 0x402050 */
        void (*rax)() ();
    }
    if (*((rbp - 4)) != 0x7d) {
        goto label_0;
        eax = 0;
        printf ("Block 2");
        goto label_1;
        eax = 0;
        printf ("Block 3");
        goto label_1;
        eax = 0;
        printf ("Block 4");
        goto label_1;
        eax = 0;
        printf ("Block 5");
        goto label_1;
        eax = 0;
        printf ("Block 6");
    } else {
        eax = 0;
        printf ("Block 7");
        goto label_1;
label_0:
        eax = 0;
        printf ("Block 8");
    }
label_1:
    eax = 0;
    printf ("Block 9");
    return rax;
}



int32_t test_2 (uint32_t arg1, uint32_t arg2) {
    uint32_t var_8h;
    uint32_t var_4h;
    rdi = arg1;
    rsi = arg2;
    *((rbp - 4)) = edi;
    *((rbp - 8)) = esi;
    eax = 0;
    printf ("Block 1");
    if (*((rbp - 4)) == 1) {
        if (*((rbp - 8)) == 1) {
            eax = 0;
            printf ("Block 3");
        }
    } else {
        eax = 0;
        printf ("Block 2");
    }
    if (*((rbp - 4)) == 1) {
        eax = 0;
        printf ("Block 5");
    } else {
        eax = 0;
        printf ("Block 4");
    }
    eax = 0;
    printf ("Block 6");
    eax = 0;
    return eax;
}



int32_t test_3 (signed int64_t arg1, signed int64_t arg2, signed int64_t arg3) {
    signed int64_t var_ch;
    signed int64_t var_8h;
    signed int64_t var_4h;
    rdi = arg1;
    rsi = arg2;
    rdx = arg3;
    *((rbp - 4)) = edi;
    *((rbp - 8)) = esi;
    *((rbp - 0xc)) = edx;
    eax = 0;
    printf (0x402088);
    goto label_1;
label_0:
    eax = 0;
    printf (0x40208b);
    while (*((rbp - 4)) <= 0x13) {
        eax = 0;
        printf (0x40208e);
        if (*((rbp - 0xc)) <= 0x31) {
            goto label_2;
        }
        eax = 0;
        printf (0x402091);
    }
label_1:
    if (*((rbp - 8)) <= 0x63) {
        goto label_0;
    }
    goto label_3;
label_2:
label_3:
    eax = 0;
    printf (0x402094);
    return eax;
}



int32_t test_4 (uint32_t arg1, signed int64_t arg2) {
    signed int64_t var_8h;
    uint32_t var_4h;
    rdi = arg1;
    rsi = arg2;
    *((rbp - 4)) = edi;
    *((rbp - 8)) = esi;
    eax = 0;
    printf ("Block 1");
    while (*((rbp - 4)) == 1) {
        eax = 0;
        printf ("Block 3");
        if (*((rbp - 8)) <= 4) {
            eax = 0;
            printf ("Block 4");
        } else {
            eax = 0;
            printf ("Block 5");
            if (*((rbp - 8)) > 9) {
                goto label_1;
            }
            goto label_0;
        }
label_1:
        eax = 0;
        printf ("Block 6");
label_0:
    }
    eax = 0;
    printf ("Block 2");
    if (*((rbp - 8)) <= 0x13) {
        goto label_0;
    }
    eax = 0;
    printf ("Block 7");
    eax = 0;
    return eax;
}
