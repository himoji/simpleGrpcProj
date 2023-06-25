from concurrent import futures
import logging

import grpc
import GreetingService_pb2_grpc
import GreetingService_pb2

class Greeter(GreetingService_pb2_grpc.GreetingServiceServicer):

    def greeting(self, request, context):
        print(request, context)

        return GreetingService_pb2.HelloResponce(greeting="hello!!!!")

        #return super().greeting(request, context)
    

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GreetingService_pb2_grpc.add_GreetingServiceServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()