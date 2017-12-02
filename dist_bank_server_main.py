# MainServer.py
# The main server of the service.

from concurrent import futures
import time
import grpc
import dist_bank_pb2_grpc
import dist_bank_pb2
import dist_bank_resources

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def get_record(dist_bank_db, uid):
    """
    This helper function is used to get a record from the database.
    If record does not exist, then return None. Further operation on this will
    be dealt with by outer scope function which calls this helper function.

    dist_bank_db: list, self.db
             uid: string, user account number
          return: message BalanceRecord
    """
    for record in dist_bank_db:
        if record.uid == uid:
            return record
    return None


class DistBankServicer(dist_bank_pb2_grpc.DistBankServicer):
    """
    Provides methods that implement functionality of dist bank server.
    """
    def __init__(self):
        """
        Load account data
        """
        self.db = dist_bank_resources.read_dist_bank_database()
        # print(type(self.db))    <-- type: <class 'list'>
        # print(type(self.db[0])) <-- type: <class 'dist_bank_pb2.BalanceRecord'>
        # print(self.db)

    # TODO: Implement other methods.
    def LookUpAccount(self, request, context):
        """
        Implementation of look up account balance method.
        request: A LookUpRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        print('LookUpAccount')


    def Withdraw(self, request, context):
        """
        Implementation of withdraw money method.
        request: A WithdrawRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        print('Withdraw')

    def Save(self, request, context):
        """
        Implementation of save money method.
        request: A SaveRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        print('Save')


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