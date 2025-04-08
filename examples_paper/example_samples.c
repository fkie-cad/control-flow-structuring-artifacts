#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// test8 before
void test_1(int x){
    printf("Block 1");
    switch(x){
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
        case 125:
            printf("Block 7");
            break;
        default:
            printf("Block 8");
    }
    printf("Block 9");
}

// test17 before --> But O3
int test_2(int x, int y){
    printf("Block 1");
    if(x == 1 && y == 1){
        printf("Block 3");
    }else{
        printf("Block 2");
    }
    if(x == 1){
        printf("Block 5");
    }else{
        printf("Block 4");
    }
    printf("Block 6");
    return 0;
}

// test_2 before
void test_3(int i, int numb, int last){
    printf("B1");
    while(numb < 100){
        printf("B2");
        while(i < 20){
            printf("B3");
            if(last < 50){
                goto end_loop;
            }
            printf("B4");
        }
    }
end_loop:
    printf("B5");
}


// test_18 before
int test_4(int x, int y){
    printf("Block 1");
    do{
        while(x == 1){
            printf("Block 3");
            if(y < 5){
                printf("Block 4");
            }else{ // y >= 5
                printf("Block 5");
                if(y < 10){
                    continue;
                }
            }
            printf("Block 6");
        }
        printf("Block 2");
    }while(y < 20);
    printf("Block 7");
    return 0;
}


int main(){
    return 0;
}
