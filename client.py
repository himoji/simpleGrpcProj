import grpc
import bank_pb2
import bank_pb2_grpc

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

def rundeposit() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = bank_pb2_grpc.bankStub(channel)
        # Read from an generator

        response = stub.deposit(bank_pb2.depositRequest(customer_id=1, cash_amount=123))
    print(f"Validation: {response.valid}")

def runwithdraw() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = bank_pb2_grpc.bankStub(channel)
        # Read from an generator

        response = stub.deposit(bank_pb2.depositRequest(customer_id=1, cash_amount=123))
    print(f"Validation: {response.valid}")

def runsend() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = bank_pb2_grpc.bankStub(channel)
        # Read from an generator

        response = stub.deposit(bank_pb2.depositRequest(customer_id=1, cash_amount=123, taker_id=2))
    print(f"Validation: {response.valid}")

if __name__ == "__main__":
    runwithdraw()