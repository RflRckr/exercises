#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>

#define MAX_THREADS 2
#define SIZE 20

sem_t cheio;
sem_t vazio;
sem_t lock_cons;
sem_t lock_prod;
int buff[SIZE];
int cont = 0;
int i = 0;
int f = 0;
void *Produtor() {
	while(1) {
		sem_wait(&vazio);
		sem_wait(&lock_prod);
		++cont;
		f = (f+1) % SIZE;
		buff[f] = cont;
		printf("Prodduzido = %d \n", buff[f]);
		sem_post(&lock_prod);
		sem_post(&cheio);
	}
}
void *Consumidor() {
	while(1) {
		sem_wait(&cheio);
		sem_wait(&lock_cons);
		i = (i+1) % SIZE;
		printf("Consumido = %d \n", buff[i]);
		sem_post(&lock_cons);
		sem_post(&vazio);
	}
}

int main(int argc, char const *argv[]) {
	int i;
	pthread_t threads[MAX_THREADS];
	pthread_t threadsC[MAX_THREADS];
	sem_init(&cheio, 0, 0);
	sem_init(&vazio, 0, SIZE);
	sem_init(&lock_prod, 0, 1);
	sem_init(&lock_cons, 0, 1);
	for(i = 0; i < MAX_THREADS; i++) {
		pthread_create(&threads[i], NULL, Produtor, NULL);
	}
	for(i = 0; i < MAX_THREADS; i++) {
		pthread_create(&threadsC[i], NULL, Consumidor, NULL);
	}
	for(i = 0; i < MAX_THREADS; i++) {
		pthread_join(threads[i], NULL);
	}
	for(i = 0; i < MAX_THREADS; i++) {
		pthread_join(threadsC[i], NULL);
	}
	sem_destroy(&vazio);
	sem_destroy(&cheio);
	sem_destroy(&lock_prod);
	sem_destroy(&lock_cons);
	return 0;
}
