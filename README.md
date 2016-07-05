# RPC with RPCGEN

In order to successfully compile and run the code from this repository do the following:

### Compiling

```sh
$ gcc -c client.c -o client.o
$ gcc -c square_clnt.c -o square_clnt.o
$ gcc -c square_xdr.c -o square_xdr.o
$ gcc -o client client.o square_clnt.o square_xdr.o
$ gcc -c client.c server.c square_xdr.c
$ gcc -c server.c -o server.o
$ gcc -c square_svc.c -o square_svc.o
$ gcc -o server server.o square_svc.o square_xdr.o
$ ./server &
$ ./client localhost 4
```

Then it should display: ```result: 16```
