// angr 9.2.146 using DREAM restructuring as in scripts

int test_1(unsigned int a0)
{
    printf("Block 1");
    if (a0 <= 6)
    {
        if (a0 >= 2)
        {
            switch (a0)
            {
                case 2:
                    printf("Block 2");
                    break;
                case 3:
                    printf("Block 3");
                    break;
                case 4:
                    printf("Block 4");
                    break;
                case 5:
                    printf("Block 5");
                    break;
                case 6:
                    printf("Block 6");
                    break;
                default:
                    printf("Block 8");
            }
        }
    }
    else
    {
        if (a0 == 125)
            printf("Block 7");
    }
    printf("Block 8");
    return printf("Block 9");
}



long long test_2(unsigned int a0, unsigned int a1)
{
    printf("Block 1");
    if (a0 == 1 && a1 == 1)
        printf("Block 3");
    if (a0 != 1 || a1 != 1)
        printf("Block 2");
    if (a0 == 1)
        printf("Block 5");
    else
        printf("Block 4");
    printf("Block 6");
    return 0;
}



int test_3(unsigned int a0, unsigned int a1, unsigned int a2)
{
    printf("B1");
    while (true)
    {
        printf("B2");
        while (a0 <= 19)
        {
            printf("B3");
            if (a2 <= 49)
                break;
            printf("B4");
        }
        if (true)
            return printf("B5");
    }
    return printf("B5");
}



long long test_4(unsigned int a0, unsigned int a1)
{
    printf("Block 1");
    while (true)
    {
        if (a0 == 1)
        {
            printf("Block 3");
            if (a1 <= 4)
            {
                printf("Block 4");
            }
            else
            {
                printf("Block 5");
                continue;
            }
            printf("Block 6");
        }
        else
        {
            printf("Block 2");
            if (a1 > 19)
                break;
        }
    }
    printf("Block 7");
    return 0;
}
