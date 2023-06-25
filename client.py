import asyncio
import logging

import grpc
import GreetingService_pb2
import GreetingService_pb2_grpc

"""def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")

    with grpc.insecure_channel('localhost:50051') as channel:

        stub = GreetingService_pb2_grpc.GreetingServiceStub(channel)
        response = stub.greeting(GreetingService_pb2.HelloRequest(name=f'{__name__}', hobbies=['qwe', 'qwesssssssssqw']))

    print("Greeter client received: " + response.greeting)

def runStream() -> None:
    with grpc.insecure_channel('localhost:50051') as channel:

        stub = GreetingService_pb2_grpc.GreetingServiceStub(channel)
        for response in stub.greeting(GreetingService_pb2.HelloRequest(name=f'{__name__}', hobbies=['qwe', 'qwesssssssssqw'])):
            print("Greeter client received: " + response.greeting)
            
if __name__ == '__main__':
    
    logging.basicConfig()
    runStream()"""

async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = GreetingService_pb2_grpc.GreetingServiceStub(channel)
        # Read from an async generator
        async for response in stub.greeting(
            GreetingService_pb2.HelloRequest(name="you")):
            print("Greeter client received from async generator: " +
                response.greeting)
            

        # Direct read from the stub
        hello_stream = stub.greeting(
            GreetingService_pb2.HelloRequest(name="you"))
        while True:
            response = await hello_stream.read()
            if response == grpc.aio.EOF:
                break
            print("Greeter client received from direct read: " +
                response.greeting)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())