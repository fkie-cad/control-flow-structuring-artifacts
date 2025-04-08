// angr 9.2.146 using DREAM restructuring as in scripts

int test_1(unsigned int a0)
{
    printf("Block 1");
    if (a0 <= 6)
    {
        if (a0 > 1)
        {
            switch (a0)
            {
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
        }
    }
    else
    {
        if (a0 == 125)
        {
            printf("Block 7");
            return printf("Block 9");
        }
    }
    if (a0 <= 1 && a0 <= 6 || a0 > 6 && a0 != 125)
    {
        printf("Block 8");
        return printf("Block 9");
    }
}



long long test_2(unsigned int a0, unsigned int a1)
{
    printf("Block 1");
    if (a0 == 1 && a1 == 1)
        printf("Block 3");
    if (a0 != 1 || a1 != 1)
    {
        printf("Block 2");
        if (a0 != 1)
            printf("Block 4");
    }
    if (a0 == 1 || a0 == 1 && a1 == 1)
        printf("Block 5");
    printf("Block 6");
    return 0;
}



int test_3(unsigned int a0, unsigned int a1, unsigned int a2)
{
    printf("B1");
    if (a1 <= 99)
    {
        if (a0 > 19)
        {
            while (true)
            {
                printf("B2");
                printf("B2");
            }
        }
        else
        {
            printf("B2");
            if (a2 > 49)
            {
                while (true)
                {
                    printf("B3");
                    printf("B4");
                }
            }
            else
            {
                printf("B3");
            }
        }
    }
    if (a1 > 99 || a0 <= 19 && a2 <= 49)
        return printf("B5");
}



long long test_4(unsigned int a0, unsigned int a1)
{
    printf("Block 1");
    if (a0 != 1)
    {
        if (a1 <= 19)
        {
            while (true)
            {
                printf("Block 2");
            }
        }
        else
        {
            printf("Block 2");
            printf("Block 7");
            return 0;
        }
    }
    else
    {
        if (a1 <= 4)
        {
            while (true)
            {
                printf("Block 3");
                printf("Block 4");
                printf("Block 6");
            }
        }
        else if (a1 > 9)
        {
            while (true)
            {
                printf("Block 3");
                printf("Block 5");
                printf("Block 6");
            }
        }
        else
        {
            while (true)
            {
                printf("Block 3");
                printf("Block 5");
            }
        }
    }
}
