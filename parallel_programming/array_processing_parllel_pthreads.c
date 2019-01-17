#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

#define ARRAY_ELEMENT_LIMIT 10u
#define n 20000u
#define m 20000u
#define NR_THREADS 10u

struct thread_data {
	int start;
	int end;
	int threadID;
	uint64_t partialSum;
};

struct thread_data thread_data_array[NR_THREADS]

int array[n][m];
uint64_t sum = 0;

void *doPartialSum(void *data){
	int i, j;
	
	thread_data input = *((thread_data *)data);
	
	input.partialSum = 0;
	
	for (i = input.start; i<
		for(j = 0; j<n; j++) {
			input.partialSum = input.partialSum + array[i][j];
		}
	}
	
	pthread_exist(NULL);
}

/* Initialize each element in the array with a random element between 0 and ARRAY_ELEMENT_LIMIT */
void initializeArray(void){
    int i, j;
    
    /*Initialize seed*/
    srand(time(NULL));

    for (i = 0; i<n; i++){
        for (j = 0; j<m; j++){
            array[i][j] = rand() % ARRAY_ELEMENT_LIMIT;
            //printf("%d ", array[i][j]);
        }
        //printf("\n");
    }
}

int main(){
    struct timespec start, end;
	uint64_t delta_us;
	pthread_t threads[NR_THREADS];
	pthread_attr_t attr;
	int rc;
	
	clock_gettime(CLOCK_MONOTONIC, &start);

    /* Insert code below for measurement*/
    int t;

    initializeArray();
	
	/* Initialize and set thread detached attribute */
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

    for (t = 0; t<NR_THREADS; t++){
		thread_data_array[t].start = (n/NR_THREADS)*t;
		thread_data_array[t].end = (n/NR_THREADS)*(t+1);
		read_data_array[t].threadID = t;
		
		rc = pthread_create(&threads[t], &attr, doPartialSum, (void *)&thread_data_array[t]);
		
		if (rc){
          printf("ERROR; return code from pthread_create() is %d\n", rc);
          return -1;
       }
	}
	
	for (t = 0; t<NR_THREADS; t++){
	
	/* Free attribute and wait for the other threads */
    pthread_attr_destroy(&attr);

	pthread_exit(NULL);
	
    printf("Sum of array elements is %hu", sum);
    /* End code measurement */
	
    clock_gettime(CLOCK_MONOTONIC, &end);
	delta_us = (end.tv_sec - start.tv_sec) * 1000 + (end.tv_nsec - start.tv_nsec) / 1000000;

    printf("\n\nExecution time:\n%hu ms\n%hu ms\n", delta_us / 1000, delta_us % 1000);

    return 0;
}
