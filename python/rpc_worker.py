"""
This module implements a worker for accessing RPC-server with threads
"""
import requests
import json
from threading import Thread


class RPCWorker(Thread):
    """
    Worker class for threads to access RPC-server
    """
    def __init__(self, queue):
        """
        Instancing thread and setting queue
        """
        Thread.__init__(self)
        self.queue = queue
        self.url = "http://localhost:4000/jsonrpc"
        self.headers = {"content-type": "application/json"}

    def run(self):
        """
        Running all tasks in queue
        """
        while True:
            rpc_data = self.queue.get()
            payload = {"method": rpc_data["method"],
                       "params": rpc_data["params"],
                       "jsonrpc": "2.0",
                       "id": 0}
            response = requests.post(self.url,
                                     data=json.dumps(payload),
                                     headers=self.headers)
            rpc_data["result"] = json.loads(response.content)["result"]
            self.queue.task_done()
