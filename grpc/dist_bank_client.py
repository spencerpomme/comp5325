# dist_bank_client.py
"""
The Python implementation of the gRPC dist bank client.
"""
import random
import time
import grpc
import dist_bank_pb2
import dist_bank_pb2_grpc
import dist_bank_resources

from dist_bank_exceptions import *

# Global variable
PORTS = ['localhost:50051', 'localhost:50052']

def bank_lookup_account(stub, request):
    """
    Client side method to request a lookup operation.

       stub: stub
    request: <class 'dist_bank_pb2.LookupRequest'
     return:
    """
    # print("In method bank_lookup_account:")
    result = stub.LookUpAccount(request) # <-- remember to check whether port is occupied!
    # from line 26 to 28 seem never gonna be reached!
    if result is None:
        return "Unable to find record"
        # raise AccountNotExistError
    # print(result)
    return result


def bank_withdraw_money(stub, request):
    """
    Client side method to request a withdraw operation.

       stub: stub
    request: <class 'dist_bank_pb2.WithdrawRequest'
     return:
    """
    # print("In method bank_withdraw_money:")
    try:
        result = stub.Withdraw(request)
    except DatabaseOptFailure:
        return "IO_Failure"
    return result


def bank_save_money(stub, request):
    """
    Client side method to request a save operation.

       stub: stub
    request: <class 'dist_bank_pb2.SaveRequest'
     return:
    """
    # print("In method bank_withdraw_money:")
    try:
        result = stub.Save(request)
    except DatabaseOptFailure:
        return "IO_Failure"
    return result


def server_prober(stub, request):
    """
    Try to connect to server.
    This method shall not be called by client.
    """
    try:
        status = stub.ProbeStatus(request)
    except Exception as e:
        shift_server()
    else:
        return 1


def shift_server():
    """
    This method is change port when current connected server is down.
    """
    pass







def run(t_uid="5a221afc35b38f9a0ba44b2c"):
    """
    Simple client runability tests.
    """
    print('FUCK')
    channel = grpc.insecure_channel('localhost:50051')
    print(dir(channel))
    stub = dist_bank_pb2_grpc.DistBankStub(channel)
    print(dir(stub))

    print("-------------- Probe Server----------------")
    if server_prober(stub, dist_bank_pb2.ProbeRequest(hey="hey!")):
        print("hhahahahahahahahah")

    print("-------------- LookupAccount --------------")
    print(bank_lookup_account(stub, dist_bank_pb2.LookUpRequest(uid=t_uid)))

    print("------------------- withdraw --------------")
    print(bank_withdraw_money(stub, dist_bank_pb2.WithdrawRequest(uid=t_uid, with_amount=2000000.0)))

    print("-------------- LookupAccount --------------")
    print(bank_lookup_account(stub, dist_bank_pb2.LookUpRequest(uid=t_uid)))

    print("------------------ save -------------------")
    print(bank_save_money(stub, dist_bank_pb2.SaveRequest(uid=t_uid, save_amount=100.0)))

    print("-------------- LookupAccount --------------")
    print(bank_lookup_account(stub, dist_bank_pb2.LookUpRequest(uid=t_uid)))


if __name__ == '__main__':
    run()


"""
The target test data:
{

    "balance": "62415.24",
    "index": 66,
    "uid": "5a221afc35b38f9a0ba44b2c"
  }
"""