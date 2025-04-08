// Version 9.1.0.250226

//----- (0000000000401150) ----------------------------------------------------
int __fastcall test_1(int a1)
{
    int result; // eax

    printf("Block 1");
    if ( a1 > 6 )
    {
        if ( a1 == 125 )
        {
            printf("Block 7");
            return printf("Block 9");
        }
        goto LABEL_10;
    }
    if ( a1 <= 1 )
    {
        LABEL_10:
        printf("Block 8");
        return printf("Block 9");
    }
    switch ( a1 )
    {
        case 3:
            printf("Block 3");
            result = printf("Block 9");
            break;
        case 4:
            printf("Block 4");
            result = printf("Block 9");
            break;
        case 5:
            printf("Block 5");
            result = printf("Block 9");
            break;
        case 6:
            printf("Block 6");
            result = printf("Block 9");
            break;
        default:
            printf("Block 2");
            result = printf("Block 9");
            break;
    }
    return result;
}



//----- (0000000000401270) ----------------------------------------------------
__int64 __fastcall test_2(int a1, int a2)
{
    printf("Block 1");
    if ( a1 == 1 && a2 == 1 )
    {
        printf("Block 3");
    }
    else
    {
        printf("Block 2");
        if ( a1 != 1 )
        {
            printf("Block 4");
            goto LABEL_5;
        }
    }
    printf("Block 5");
    LABEL_5:
    printf("Block 6");
    return 0;
}



//----- (00000000004012E0) ----------------------------------------------------
int __fastcall test_3(int a1, int a2, int a3)
{
    printf("B1");
    if ( a2 <= 99 )
    {
        if ( a1 > 19 )
        {
            while ( 1 )
            {
                printf("B2");
                printf("B2");
            }
        }
        printf("B2");
        if ( a3 > 49 )
        {
            while ( 1 )
            {
                printf("B3");
                printf("B4");
            }
        }
        printf("B3");
    }
    return printf("B5");
}



//----- (0000000000401380) ----------------------------------------------------
__int64 __fastcall test_4(int a1, int a2)
{
    printf("Block 1");
    if ( a1 == 1 )
    {
        if ( a2 > 4 )
        {
            if ( a2 > 9 )
            {
                while ( 1 )
                {
                    printf("Block 3");
                    printf("Block 5");
                    printf("Block 6");
                }
            }
            while ( 1 )
            {
                printf("Block 3");
                printf("Block 5");
            }
        }
        while ( 1 )
        {
            printf("Block 3");
            printf("Block 4");
            printf("Block 6");
        }
    }
    if ( a2 <= 19 )
    {
        while ( 1 )
            printf("Block 2");
    }
    printf("Block 2");
    printf("Block 7");
    return 0;
}
