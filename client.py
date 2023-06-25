from __future__ import print_function

import logging

import grpc
import GreetingService_pb2
import GreetingService_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")

    with grpc.insecure_channel('localhost:50051') as channel:

        stub = GreetingService_pb2_grpc.GreetingServiceStub(channel)
        response = stub.greeting(GreetingService_pb2.HelloRequest(name='you', hobbies=['qwe', 'qweqw']))

    print("Greeter client received: " + response.greeting)


if __name__ == '__main__':
    
    logging.basicConfig()
    run()