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

struct thread_data thread_data_array[NR_THREADS];

int array[n][m];
uint64_t sum = 0;

void *doPartialSum(void *data){
	int i, j;
	
	struct thread_data *my_data;

	my_data = (struct thread_data *)data;
	
	my_data->partialSum = 0;
	
	for (i = my_data->start; i<my_data->end; i++) {
		for(j = 0; j<m; j++) {
			my_data->partialSum = my_data->partialSum + array[i][j];
		}
	}
	
	//printf("Thread: Thread %d done.\n", my_data->threadID);
	pthread_exit(NULL);
}

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

int main(){
    struct timespec start, end;
	uint64_t delta_us;
	pthread_t threads[NR_THREADS];
	pthread_attr_t attr;
	int rc;
	int tmp_index;
	void * status;
	
	clock_gettime(CLOCK_MONOTONIC, &start);

    /* Insert code below for measurement*/
    int t;

    initializeArray();
	
	/* Initialize and set thread detached attribute */
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

	tmp_index = 0;
	
    for (t = 0; t<NR_THREADS; t++){
		thread_data_array[t].start = tmp_index;
		if (tmp_index + (n/NR_THREADS) <= n) {
			thread_data_array[t].end = tmp_index + (n/NR_THREADS);
			tmp_index = thread_data_array[t].end;
			//printf("Main: Thread %d index start = %d, index end = %d\n", t, thread_data_array[t].start, thread_data_array[t].end);
		} else {
			thread_data_array[t].end = n;
			t = NR_THREADS;
		}
		
		thread_data_array[t].threadID = t;
		
		rc = pthread_create(&threads[t], &attr, doPartialSum, (void *)&thread_data_array[t]);
		if (rc){
          printf("ERROR; return code from pthread_create() is %d\n", rc);
          return -1;
       }
	}
	
	/* Free attribute and wait for the other threads */
    pthread_attr_destroy(&attr);
	
	/* Retrieve the partial results from the threads */
	for (t = 0; t<NR_THREADS; t++){
		rc = pthread_join(threads[t], &status);
		if (rc) {
			printf("ERROR: return code from pthread_join() is %d\n", rc);
			return -1;
		}
		
		sum += thread_data_array[t].partialSum;
		
		//printf("Main: Thread %ld completed, adding partial result!\n", t);
	}
	
    printf("Main: Sum of array elements is %lu", sum);
    /* End code measurement */
	
    clock_gettime(CLOCK_MONOTONIC, &end);
	delta_us = (end.tv_sec - start.tv_sec) * 1000 + (end.tv_nsec - start.tv_nsec) / 1000000;

    printf("\n\nExecution time:\n%lu ms\n%lu ms\n", delta_us / 1000, delta_us % 1000);

    pthread_exit(NULL);
}
