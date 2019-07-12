import logging

import grpc

from pygrpcspec.proto import todo_pb2_grpc
from pygrpcspec.proto import todo_pb2

def run():
    port = 5555
    with grpc.insecure_channel('localhost:'+str(port)) as channel:
        todoClient = todo_pb2_grpc.TaskManagerStub(channel)
        response = todoClient.GetSummary(todo_pb2.Employee(name='Employee1'))
    print("GetSummary response: ", response)

if __name__ == '__main__':
    logging.basicConfig()
    run()
