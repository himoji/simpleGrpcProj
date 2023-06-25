
import logging, asyncio
import time

import grpc


from GreetingService_pb2 import HelloResponce
from GreetingService_pb2 import HelloRequest
from GreetingService_pb2_grpc import GreetingServiceServicer
from GreetingService_pb2_grpc import add_GreetingServiceServicer_to_server

"""class Greeter(GreetingService_pb2_grpc.GreetingServiceServicer):
    def greeting(self, request, context):
        print(f"req: {request}")

        for i in range(10):
            yield GreetingService_pb2.HelloResponce(greeting=f"hello responce, {request.name}")
            time.sleep(0.1)

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
    serve()"""

class Greeter(GreetingServiceServicer):

    async def greeting(self, request: HelloRequest,
                       context: grpc.aio.ServicerContext) -> HelloResponce:
        logging.info("Serving sayHello request %s", request)

        for i in range(10):
            time.sleep((10-i)/10)# tf this is going 0 to 9, not 9 to 0, async???
            yield HelloResponce(greeting=f"Hello number {i}, {request.name}!")


async def serve() -> None:
    server = grpc.aio.server()
    add_GreetingServiceServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())