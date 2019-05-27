#include <stdio.h>
#include <pthread.h>

#define MAX_THREADS 10

int var_compartilhada = 0;

pthread_mutex_t mutex_global;

void *func(void *argumento) {
	int i;
	pthread_t tid = pthread_self();	
	
	for(i = 0; i < 100; i++) {
		pthread_mutex_lock(&mutex_global);
		var_compartilhada++;
		pthread_mutex_unlock(&mutex_global);
	}
	printf("Thread %ld: var_compartilhada = %d.\n", (long)tid, var_compartilhada);
	return 0;
}

int main(int argc, char **argv) {
	int i;
	pthread_t threads[MAX_THREADS];

	pthread_mutex_init(&mutex_global, NULL);

	printf("Main thread iniciada.\n");

	for(i = 0; i < MAX_THREADS; i++)
		pthread_create(&threads[i], NULL, func, NULL);

	for(i = 0; i < MAX_THREADS; i++)
		pthread_join(threads[i], NULL);

	printf("Main thread: var_compartilhada = %d.\n", var_compartilhada);

	pthread_mutex_destroy(&mutex_global);

	return 0;
}
