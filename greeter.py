import GreetingService_pb2_grpc, GreetingService_pb2
import grpc

class Greeter(GreetingService_pb2_grpc.GreetingServiceServicer):
    NUMBER_OF_REPLY = 10

    def greeting(self, request, context):
        print(f"req: {request}")

        return GreetingService_pb2.HelloResponce(greeting=f"hello responce, {request.name}")

        #return super().greeting(request, context)

    def greetingStream(self, request, context):
        print(f"req: {request}")

        return GreetingService_pb2.HelloResponce(greeting=f"hello responce, {request.name}")