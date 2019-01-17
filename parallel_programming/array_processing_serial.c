#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_ELEMENT_LIMIT 50u;

int array[1000][1000];
int m, n;
int sum = 0;

/* Initialize each element in the array with a random element between 0 and ARRAY_ELEMENT_LIMIT */
void initializeArray(void){
    int i, j;
    
    /*Initialize seed*/
    srand(time(NULL));

    for (i = 0; i<n; i++){
        for (j = 0; j<m; j++){
            array[i][j] = rand() % ARRAY_ELEMENT_LIMIT;
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}

void fnc(int a, int b){
    sum = sum + array[a][b];
}

int main(){
    clock_t begin = clock();

    /* Insert code below for measurement*/
    int i, j;

    printf("What is the size of the 2-dimensional array?\n");
    scanf("%d %d", &n, &m);

    initializeArray();

    for (i = 0; i<n; i++){
        for (j = 0; j<n; j++){
            fnc(i,j);
        }
    }

    printf("\nSum of array elements is %d", sum);

    /* End code measurement */

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

    printf("\n\nExecution time: %g", time_spent);

    return 0;
}
