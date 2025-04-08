// Binary Ninja Version 4.2.6455

int64_t test_1(int32_t arg1)

{
    printf("Block 1");

    if (arg1 > 6)
    {
        if (arg1 == 0x7d)
            printf("Block 7");
        else
            printf("Block 8");
    }
    else if (arg1 < 2 || arg1 > 6)
        printf("Block 8");
    else
        switch (arg1)
        {
            case 0:
            case 1:
            {
                printf("Block 8");
                break;
            }
            case 2:
            {
                printf("Block 2");
                break;
            }
            case 3:
            {
                printf("Block 3");
                break;
            }
            case 4:
            {
                printf("Block 4");
                break;
            }
            case 5:
            {
                printf("Block 5");
                break;
            }
            case 6:
            {
                printf("Block 6");
                break;
            }
        }

        return printf("Block 9");
}



int64_t test_2(int32_t arg1, int32_t arg2)

{
    printf("Block 1");

    if (arg1 != 1 || arg2 != 1)
        printf("Block 2");
    else
        printf("Block 3");

    if (arg1 != 1)
        printf("Block 4");
    else
        printf("Block 5");

    printf("Block 6");
    return 0;
}



int64_t test_3(int32_t arg1, int32_t arg2, int32_t arg3)

{
    printf("B1");

    while (arg2 <= 0x63)
    {
        printf("B2");

        while (arg1 <= 0x13)
        {
            printf("B3");

            if (arg3 <= 0x31)
                return printf("B5");

            printf("B4");
        }
    }

    return printf("B5");
}



int64_t test_4(int32_t arg1, int32_t arg2)

{
    printf("Block 1");

    while (true)
    {
        if (arg1 == 1)
        {
            printf("Block 3");

            if (arg2 > 4)
            {
                printf("Block 5");

                if (arg2 <= 9)
                    continue;
            }
            else
                printf("Block 4");

            printf("Block 6");
        }
        else
        {
            printf("Block 2");

            if (arg2 > 0x13)
                break;
        }
    }

    printf("Block 7");
    return 0;
}
