    struct rpc_args {
     int *vector_slice;
     int slice_size;
     };
    
    struct square_out {
    long    res1;
    };
    
    program SQUARE_PROG {
    version SQUARE_VERS {
    square_out  SQUAREPROC(rpc_args) = 1;
                        /* procedure number = 1 */
    } = 1;              /* version number = 1 */
    } = 0x31230000;         /* program number = 0x31230000 */
