// Version r2-5.9.9 and r2pm-5.9.9 and r2dec 40899cd960ae198ebf841ddf410014fddd1ed831

int32_t test_1 (int64_t arg1) {
    rdi = arg1;
    eax = 0;
    ebx = edi;
    eax = printf ("Block 1");
    if (ebx <= 6) {
        if (ebx <= 1) {
            goto label_0;
        }
        ebx -= 3;
        if (ebx > 3) {
            goto label_1;
        }
        /* switch table (4 cases) at 0x402060 */
    }
    if (ebx == 0x7d) {
        eax = 0;
        eax = printf ("Block 7");
        edi = "Block 9";
        eax = 0;
        void (*0x401030)() ();
        eax = 0;
        eax = printf ("Block 6");
        edi = "Block 9";
        eax = 0;
        void (*0x401030)() ();
        eax = 0;
        eax = printf ("Block 5");
        edi = "Block 9";
        eax = 0;
        void (*0x401030)() ();
        eax = 0;
        eax = printf ("Block 3");
        edi = "Block 9";
        eax = 0;
        void (*0x401030)() ();
        eax = 0;
        eax = printf ("Block 4");
        edi = "Block 9";
        eax = 0;
        void (*0x401030)() ();
    }
label_0:
    eax = 0;
    eax = printf ("Block 8");
    edi = "Block 9";
    eax = 0;
    void (*0x401030)() ();
label_1:
    eax = 0;
    eax = printf ("Block 2");
    edi = "Block 9";
    eax = 0;
    return printf ();
}



int32_t test_2 (int64_t arg1, int64_t arg2) {
    rdi = arg1;
    rsi = arg2;
    eax = 0;
    ebx = edi;
    eax = printf ("Block 1");
    if (ebx != 1) {
        goto label_1;
    }
    if (ebp != 1) {
        goto label_1;
    }
    eax = 0;
    eax = printf ("Block 3");
    do {
        eax = 0;
        eax = printf ("Block 5");
label_0:
        eax = 0;
        eax = printf ("Block 6");
        eax = 0;
        return eax;
label_1:
        eax = 0;
        eax = printf ("Block 2");
    } while (ebx == 1);
    eax = 0;
    printf ("Block 4");
    goto label_0;
}



uint64_t test_3 (int64_t arg1, int64_t arg2, int64_t arg3) {
    rdi = arg1;
    rsi = arg2;
    rdx = arg3;
    eax = 0;
    r12d = edi;
    ebx = esi;
    eax = printf (0x40204c);
    if (ebx > 0x63) {
        goto label_0;
    }
    if (r12d <= 0x13) {
        goto label_1;
    }
    do {
        eax = 0;
        eax = printf (0x40204f);
        eax = 0;
        eax = printf (0x40204f);
    } while (1);
label_1:
    eax = 0;
    rax = printf (0x40204f);
    if (ebp <= 0x31) {
        goto label_2;
    }
    do {
        eax = 0;
        eax = printf (0x402052);
        eax = 0;
        eax = printf (0x402055);
    } while (1);
label_2:
    eax = 0;
    eax = printf (0x402052);
label_0:
    edi = 0x402058;
    eax = 0;
    return printf ();
}



int32_t test_4 (int64_t arg1, int64_t arg2) {
    rdi = arg1;
    rsi = arg2;
    eax = 0;
    ebx = esi;
    eax = printf ("Block 1");
    if (ebp == 1) {
        goto label_0;
    }
    if (ebx > 0x13) {
        goto label_1;
    }
    do {
        eax = 0;
        eax = printf ("Block 2");
    } while (1);
label_1:
    eax = 0;
    eax = printf ("Block 2");
    eax = 0;
    eax = printf ("Block 7");
    eax = 0;
    return eax;
label_0:
    if (ebx <= 4) {
        goto label_2;
    }
    if (ebx <= 9) {
        goto label_3;
    }
    do {
        eax = 0;
        eax = printf ("Block 3");
        eax = 0;
        eax = printf ("Block 5");
        eax = 0;
        eax = printf ("Block 6");
    } while (1);
    do {
label_2:
        eax = 0;
        eax = printf ("Block 3");
        eax = 0;
        eax = printf ("Block 4");
        eax = 0;
        eax = printf ("Block 6");
    } while (1);
    do {
label_3:
        eax = 0;
        eax = printf ("Block 3");
        eax = 0;
        printf ("Block 5");
    } while (1);
}
