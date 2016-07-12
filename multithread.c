#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int g = 0;

void *myThreadFun(void *vargp){
    int myId = (int)vargp;
    static int s = 0;
    ++s;
    ++g;
    printf("Thread ID: %d, Static: %d, Global: %d\n", myId, ++s, ++g);
}

int main(int argc, char *argv[]){
    if (argc != 3){
        printf("Missing arguments!\n");
        return 0;
    }
    int i;
    pthread_t tId;
    for(i=0; i<3; i++)
        pthread_create(&tId, NULL, myThreadFun, (void *)i);
    pthread_exit(NULL);
    return 0;
}
