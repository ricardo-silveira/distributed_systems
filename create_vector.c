#include <stdio.h>
#include <stdlib.h>

int main(int arcc, char **argv){
    int *my_vect;
    my_vect = malloc(10*sizeof(int));
    int i;
    for (i=0; i<=9; i++){
        printf("%d\n", my_vect[i]);
    }
    // printf("Hello world!");
    free(my_vect);
    return (0);
}
