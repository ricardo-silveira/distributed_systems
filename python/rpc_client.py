"""
This module implements a basic client for rpc
"""
from queue import Queue
from rpc_worker import RPCWorker
from random import random
#import pandas as pd
import time


if __name__ == "__main__":
    # N elements in the "vector"
    __N = 100000000
    # DataFrame variables
    index_data = []
    row_data = []
    columns = ["Time (ms)"]
    # For each K threads
    for __k in [2**__i for __i in xrange(8)]:
        print "For %d threads" % __k
        # vector slice for each thread
        vec_k = [0]*__k
        params_by_method = [("exp_diff_null_vector", {}),
                            ("random_wave", {"amplitude": 1e3, "t": 1}),
                            ("meaning_vector", {})]
        params_by_method = params_by_method[:1]
        for method_name, params in params_by_method:
            # Running 10 times for time measuring
            print "Method: %s" % method_name
            for __t in xrange(10):
                print "%d-th time" % (__t+1)
                # Starting new vector of random values
                for __i in xrange(__k):
                    vec_k[__i] = [0]*(__N/__k)
                    for __j in xrange(__N/__k):
                        vec_k[__i][__j] = random()
                queue = Queue()
                index_data.append((method_name, __k, __t))
                print vec_k[0][0]
                # starting time counter
                start_time = time.time()
                # Working with k threads
                for __x in xrange(__k):
                    worker = RPCWorker(queue)
                    worker.daemon = True
                    worker.start()
                data = vec_k
                for vec_slice in vec_k:
                    queue.put({"method": method_name,
                               "return": data,
                               "params": [vec_slice, params]})
                queue.join()
                # passed time
                d_t = time.time() - start_time
                row_data.append([d_t])
    # Exporting DataFrame
    timer_df = pd.DataFrame(data=row_data,
                            index=pd.MultiIndex.from_tuples(index_data,
                                                            names=["method",
                                                            "k threads",
                                                            "i-th iteration"]),
                                                            columns=columns)
    print "Exporting Dataframe in a pickle..."
    timer_df.to_pickle("timer_df_%d.pickle" % __N)
