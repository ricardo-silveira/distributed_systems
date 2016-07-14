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
            queue_data = self.queue.get()
            method_name = queue_data[0]
            params = queue_data[1]
            payload = {"method": method_name,
                       "params": params,
                       "jsonrpc": "2.0",
                       "id": 0}
            requests.post(self.url,
                          data=json.dumps(payload),
                          headers=self.headers)
            self.queue.task_done()
