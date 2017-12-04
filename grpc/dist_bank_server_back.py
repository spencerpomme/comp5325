# MainServer.py
# The main server of the service.

from concurrent import futures
from dist_bank_exceptions import *
import time
import grpc
import dist_bank_pb2_grpc
import dist_bank_pb2
import dist_bank_resources

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Below defines the res_infos:
_SUCCESS_RETRIVAL = '1'
_RECORD_NOT_EXIST = '0'
_NOT_ENOUGH_MONEY = '2'

# DB modification flags send from dist_bank_resources
_SUCCESS_MODIFIED = 0
_MODIFICATION_ERR = 1



def get_record(dist_bank_db, request):
    """
    This helper function is used to get a record from the database.
    If record does not exist, then return None. Further operation on this will
    be dealt with by outer scope function which calls this helper function.

    dist_bank_db: list, self.db
         request: message LookUpRequest
          return: message BalanceRecord
    """
    for record in dist_bank_db:
        if record.uid == request.uid:
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
        print('Method LookUpAccount called:')
        self.update_db()
        record = get_record(self.db, request)
        if record is None:
            return dist_bank_pb2.BalanceRecord(uid="0", balance=0, index=-1, res_info=_RECORD_NOT_EXIST)
        else:
            return record


    def Withdraw(self, request, context):
        """
        Implementation of withdraw money method.
        request: A WithdrawRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        print('Method Withdraw called:')
        self.update_db()
        record = get_record(self.db, request)
        if record is None:
            return dist_bank_pb2.BalanceRecord(uid="0",
                                               balance=0,
                                               index=-1,
                                               res_info=_RECORD_NOT_EXIST)
        else:
            look_up_request = dist_bank_pb2.LookUpRequest(uid=request.uid)
            res_flag = dist_bank_resources.modify_dist_bank_database_withdraw(request)

            if res_flag == _SUCCESS_MODIFIED:
                self.update_db()
                return get_record(self.db, look_up_request)
            else:
                print('res_flag: ', res_flag)
                # Return a not modified record:
                return dist_bank_pb2.BalanceRecord(uid=look_up_request.uid,
                                                   balance=self.LookUpAccount(request, context).balance,
                                                   index=self.LookUpAccount(request, context).index,
                                                   res_info=_RECORD_NOT_EXIST)



    def Save(self, request, context):
        """
        Implementation of save money method.
        request: A SaveRequest (see dist_bank.proto)
        return: A BalanceRecord response (see dist_bank.proto)
        """
        print('Method Save called:')
        self.update_db()
        record = get_record(self.db, request)
        if record is None:
            return dist_bank_pb2.BalanceRecord(uid="0", balance=0, index=-1, res_info=_RECORD_NOT_EXIST)
        else:
            res_flag = dist_bank_resources.modify_dist_bank_database_save(request)
            if res_flag == _SUCCESS_MODIFIED:
                self.update_db()
                # If res_flag is success, then construct a LookUpRequest to look up modified record:
                look_up_request = dist_bank_pb2.LookUpRequest(uid=request.uid)
                return get_record(self.db, look_up_request)
            else:
                print('res_flag: ', res_flag)
                raise DatabaseOptFailure


    def ProbeStatus(self, request, context):
        """
        This method is for checking server status.
        """
        print("Method ProbeStatus called!")
        return dist_bank_pb2.Status(alive=1)


    def Synchronize(self, request, context):
        """
        Method to synchronize requests.
        """
        pass

    def update_db(self):
        """
        Update after modification
        """
        self.db = dist_bank_resources.read_dist_bank_database()



def serve():
    """
    Initial server framework. Need further modifications!
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dist_bank_pb2_grpc.add_DistBankServicer_to_server(
        DistBankServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(dir(server))
    print('Server started.\n')
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


# Need a request director to redirect connection to other server when this server fails.
if __name__ == '__main__':
    serve()
