#include  <rpc/rpc.h>
#include  "square.h"
#include  "test.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>


void *myFun(void *x){
    square_out  *outp;
    thread_args *tArgs;
    tArgs = ((thread_args *) x); 
    if ( (outp = squareproc_1(&tArgs->args, tArgs->cl)) == NULL){
        printf("fuckit");
        }
        else{
    printf("hey oh!");
    printf("%ld\n", outp->res1);
    }return NULL;
}

int main(int argc, char **argv){
    CLIENT      *cl;
    rpc_args   in;

    pthread_t *threads;
    thread_args *tArgs;
    int **randomVector;

    int rc, i, j;

    // Should read from csv file
    int N = 3;
    int M = 1000000;

    // Creating randomVector
    randomVector = malloc(N*sizeof(int*));
    for (i=0; i<N; i++){
        randomVector[i] = malloc(M*sizeof(int));
        for (j=0; j<M; j++){
            randomVector[i][j] = rand()%10000;
        }
    }

    // Connecting to server
    cl = clnt_create(argv[1], SQUARE_PROG, SQUARE_VERS, "tcp");

    // Creating threads and parameters structure
    threads = (pthread_t *)malloc(sizeof(pthread_t)*N);
    tArgs = (thread_args *)malloc(sizeof(thread_args)*N);
    for(i=0; i<N; i++){
        tArgs[i].cl = cl;
        tArgs[i].args.vector_slice = randomVector[i];
        tArgs[i].args.slice_size = M;
        rc = pthread_create(&threads[i], NULL, myFun, (void *) &tArgs[i]);
    printf("aaa\n");
    }

    // Waiting threads to end
    for(i=0; i<N; i++){
        rc = pthread_join(threads[i], NULL);
    }

    //if ( (outp = squareproc_1(&in, cl)) == NULL){
    //    exit(0);}
    //printf("a");

    //printf("result: %ld\n", outp->res1);
    return (0);
}
