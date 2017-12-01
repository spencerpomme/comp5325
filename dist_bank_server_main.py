# MainServer.py
# The main server of the service.

from concurrent import futures
import time
import grpc
import dist_bank_pb2_grpc
import dist_bank_pb2
import dist_bank_resources

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DistBank(route_guide_pb2_grpc.DistBankServicer):
    """
    Provides methods that implement functionality of dist bank server.
    """
    def __init__(self):
        self.db = dist_bank_resources.read_route_guide_database()

    # TODO: Implement other methods.
    def LookUpAccount(self, request, context):
        """
        Implementation of look up account balance method.
        request: A LookUpRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        raise NotImplementedError

    def Withdraw(self, request, context):
        """
        Implementation of withdraw money method.
        request: A WithdrawRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        raise NotImplementedError

    def Save(self, request, context):
        """
        Implementation of save money method.
        request: A SaveRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        raise NotImplementedError


def serve():
    """
    Initial server framework. Need further modifications!
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dist_bank_pb2_grpc.add_DistBankServicer_to_server(
        DistBankServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()