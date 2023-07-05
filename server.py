
import logging
from concurrent.futures import ThreadPoolExecutor
import grpc

import bank_pb2_grpc, main

from bank_pb2 import withdrawRequest, sendRequest
from bank_pb2 import validationResponce
from bank_pb2_grpc import bankServicer
from bank_pb2_grpc import add_bankServicer_to_server

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


class Servicer(bankServicer):

    def deposit(self, request, context) -> validationResponce:
        print("Serving deposit:")

        main.atm.deposit(request.customer_id, request.cash_amount)

        return validationResponce(valid="true")
    
    def withdraw(self, request: withdrawRequest,
                       context) -> validationResponce:
        print(f"Serving withdraw: {request}")

        main.atm.withdraw(request.customer_id, request.cash_amount)

        return validationResponce(valid="true")

    def send(self, request: sendRequest,
                       context) -> validationResponce:
        print(f"Serving sending: {request}")

        main.atm.send(request.customer_id, request.cash_amount, request.taker_id)

        return validationResponce(valid="true")



def serve() -> None:
    port = '50051'
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    bank_pb2_grpc.add_bankServicer_to_server(Servicer(), server)

    server.add_insecure_port('[::]:' + port)
    server.start()

    print("Server started, listening on " + port)

    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()