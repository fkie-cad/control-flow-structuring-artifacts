// Version 9.1.0.250226

//----- (0000000000401136) ----------------------------------------------------
int __fastcall test_1(int a1)
{
    printf("Block 1");
    if ( a1 > 6 )
    {
        if ( a1 == 125 )
        {
            printf("Block 7");
            return printf("Block 9");
        }
        LABEL_12:
        printf("Block 8");
        return printf("Block 9");
    }
    if ( a1 < 2 )
        goto LABEL_12;
    switch ( a1 )
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
            goto LABEL_12;
    }
    return printf("Block 9");
}



//----- (0000000000401202) ----------------------------------------------------
__int64 __fastcall test_2(int a1, int a2)
{
    printf("Block 1");
    if ( a1 == 1 && a2 == 1 )
        printf("Block 3");
    else
        printf("Block 2");
    if ( a1 == 1 )
        printf("Block 5");
    else
        printf("Block 4");
    printf("Block 6");
    return 0;
}



//----- (0000000000401287) ----------------------------------------------------
int __fastcall test_3(int a1, int a2, int a3)
{
    printf("B1");
    while ( a2 <= 99 )
    {
        printf("B2");
        while ( a1 <= 19 )
        {
            printf("B3");
            if ( a3 <= 49 )
                return printf("B5");
            printf("B4");
        }
    }
    return printf("B5");
}



//----- (00000000004012FF) ----------------------------------------------------
__int64 __fastcall test_4(int a1, int a2)
{
    printf("Block 1");
    do
    {
        while ( a1 == 1 )
        {
            printf("Block 3");
            if ( a2 <= 4 )
            {
                printf("Block 4");
                goto LABEL_5;
            }
            printf("Block 5");
            if ( a2 > 9 )
                LABEL_5:
                printf("Block 6");
        }
        printf("Block 2");
    }
    while ( a2 <= 19 );
    printf("Block 7");
    return 0;
}
