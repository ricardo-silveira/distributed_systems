//#include  <rpc/rpc.h>
//#include  "square.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>


struct rpc_args{
    int *vector_slice;
    int slice_size;
};


void *myFun(void *x){
    return NULL;
}

int main(int argc, char **argv){
    //CLIENT      *cl;
    //square_in   *in;
    //square_out  *outp;
    pthread_t *threads;
    int **randomVector;

    int rc, i, j;
    
    // Should read from csv file
    int N = 3;
    int M = 3;
    
    // Creating randomVector
    randomVector = malloc(N*sizeof(int*));
    for (i=0; i<N; i++){
        randomVector[i] = malloc(M*sizeof(int));
        for (j=0; j<M; j++){
            randomVector[i][j] = rand()%10000;
            printf("%d\n", randomVector[i][j]);
        }
    }

    threads = (pthread_t *)malloc(sizeof(pthread_t)*N);
    // Creating threads
    for(i=0; i<N; i++){
        rc = pthread_create(&threads[i], NULL, myFun, (void *) &i);
    }

    // Waiting threads to end
    for(i=0; i<N; i++){
        rc = pthread_join(threads[i], NULL);
    }
    
    /*cl = clnt_create(argv[1], SQUARE_PROG, SQUARE_VERS, "tcp");

    in->arg1 = atol(argv[2]);
    if ( (outp = squareproc_1(in, cl)) == NULL)
        //err_quit("%s", clnt_sperror(cl, argv[1]));
        exit(0);

    printf("result: %ld\n", in->arg1);
    */
    return (0);
}
