"""
This module implements a json-rpc-server
"""
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
from math_functions import eulerize, amp_cosine, std_on_the_fly
import math

def exp_diff_null_vector(*args):
    vector = args[0]
    for __i in xrange(len(vector)):
        vector[__i] -= eulerize(vector[__i])


def meaning_vector(*args):
    vector = args[0]
    mean = .0
    delta = .0
    m2 = .0
    variance = .0
    for __i in xrange(len(vector)):
        vector[__i] = math.sqrt(vector[__i] - std_on_the_fly(vector[__i],
                                                             __i,
                                                             mean,
                                                             delta,
                                                             m2,
                                                             variance))

def random_wave(*args):
    vector = args[0]
    params = args[1]
    amplitude = params["amplitude"]
    t = params["t"]
    for __i in xrange(len(vector)):
        vector[__i] = amp_cosine(vector[__i], amplitude, t)


@Request.application
def application(request):
    """
    Assigning names of remote functions to dispatcher and response
    """
    dispatcher["exp_diff_null_vector"] =exp_diff_null_vector
    dispatcher["meaning_vector"] = meaning_vector
    dispatcher["random_wave"] = random_wave
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype="application/json")


if __name__ == "__main__":
    run_simple("localhost", 4000, application)
