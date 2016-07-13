#include  <rpc/rpc.h>
#include  "square.h"

struct thread_args{
    CLIENT *cl;
    rpc_args args;
};
typedef struct thread_args thread_args;

