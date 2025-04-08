// Binary Ninja Version 4.2.6455

int64_t test_1(int32_t arg1)

{
    printf("Block 1");

    if (arg1 > 6)
    {
        if (arg1 == 0x7d)
        {
            printf("Block 7");
            /* tailcall */
            return printf("Block 9");
        }
    }
    else if (arg1 > 1)
    {
        uint64_t rbx_1 = (uint64_t)(arg1 - 3);

        if (rbx_1 > 3)
        {
            printf("Block 2");
            /* tailcall */
            return printf("Block 9");
        }

        switch (rbx_1)
        {
            case 0:
            {
                printf("Block 3");
                /* tailcall */
                return printf("Block 9");
            }
            case 1:
            {
                printf("Block 4");
                /* tailcall */
                return printf("Block 9");
            }
            case 2:
            {
                printf("Block 5");
                /* tailcall */
                return printf("Block 9");
            }
            case 3:
            {
                printf("Block 6");
                /* tailcall */
                return printf("Block 9");
            }
        }
    }

    printf("Block 8");
    /* tailcall */
    return printf("Block 9");
}



int64_t test_2(int32_t arg1, int32_t arg2)

{
    printf("Block 1");

    if (arg1 != 1 || arg2 != 1)
    {
        printf("Block 2");

        if (arg1 == 1)
            printf("Block 5");
        else
            printf("Block 4");
    }
    else
    {
        printf("Block 3");
        printf("Block 5");
    }

    printf("Block 6");
    return 0;
}



int64_t test_3(int32_t arg1, int32_t arg2, int32_t arg3)

{
    printf("B1");

    if (arg2 <= 0x63)
    {
        if (arg1 <= 0x13)
        {
            printf("B2");

            if (arg3 <= 0x31)
                printf("B3");
            else
            {
                while (true)
                {
                    printf("B3");
                    printf("B4");
                }
            }
        }
        else
        {
            while (true)
            {
                printf("B2");
                printf("B2");
            }
        }
    }

    /* tailcall */
    return printf(&data_402058);
}



int64_t test_4(int32_t arg1, int32_t arg2)

{
    printf("Block 1");

    if (arg1 != 1)
    {
        if (arg2 > 0x13)
        {
            printf("Block 2");
            printf("Block 7");
            return 0;
        }

        while (true)
            printf("Block 2");
    }
    else if (arg2 <= 4)
    {
        while (true)
        {
            printf("Block 3");
            printf("Block 4");
            printf("Block 6");
        }
    }
    else if (arg2 <= 9)
    {
        while (true)
        {
            printf("Block 3");
            printf("Block 5");
        }
    }
    else
    {
        while (true)
        {
            printf("Block 3");
            printf("Block 5");
            printf("Block 6");
        }
    }
}
