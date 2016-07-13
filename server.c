    // SERVER FILE: server.c
    
    #include"rpc/rpc.h"
    #include"square.h"
    #include"stdio.h"
    #include"stdlib.h"
    #include"math.h"
    
    square_out *squareproc_1_svc(rpc_args *inp,struct svc_req *rqstp)
    {
        printf("WOW!\n");
        static square_out out;
        out.res1 = inp->vector_slice[0];
        return(&out);
    }
