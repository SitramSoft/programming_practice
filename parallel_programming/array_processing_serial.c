#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ARRAY_ELEMENT_LIMIT 10u
#define n 20000u
#define m 20000u

int array[n][m];
uint64_t sum = 0;

/* Initialize each element in the array with a random element between 0 and ARRAY_ELEMENT_LIMIT */
void initializeArray(void){
    int i, j;
    
    /*Initialize seed*/
    srand(time(NULL));

    for (i = 0; i<n; i++){
        for (j = 0; j<m; j++){
            //array[i][j] = rand() % ARRAY_ELEMENT_LIMIT;
            array[i][j] = 1;
			//printf("%d ", array[i][j]);
        }
        //printf("\n");
    }
}

void fnc(int a, int b){
    sum = sum + array[a][b];
}

int main(){
    struct timespec start, end;
	uint64_t delta_us;
	
	clock_gettime(CLOCK_MONOTONIC, &start);

    /* Insert code below for measurement*/
    int i, j;


    initializeArray();

    for (i = 0; i<n; i++){
        for (j = 0; j<m; j++){
            fnc(i,j);
        }
    }

    printf("Sum of array elements is %lu", sum);
    /* End code measurement */
	
    clock_gettime(CLOCK_MONOTONIC, &end);
	delta_us = (end.tv_sec - start.tv_sec) * 1000 + (end.tv_nsec - start.tv_nsec) / 1000000;

    printf("\n\nExecution time:\n%lu ms\n%lu ms\n", delta_us / 1000, delta_us % 1000);

    return 0;
}
