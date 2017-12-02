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


def bank_lookup_account(stub, request):
    """
    Client side method to request a lookup operation.

       stub: stub
    request: <class 'dist_bank_pb2.LookupRequest'
     return:
    """
    raise NotImplementedError


def bank_withdraw_money(stub, request):
    """
    Client side method to request a withdraw operation.

       stub: stub
    request: <class 'dist_bank_pb2.WithdrawRequest'
     return:
    """
    raise NotImplementedError


def bank_save_money(stub, request):
    """
    Client side method to request a save operation.

       stub: stub
    request: <class 'dist_bank_pb2.SaveRequest'
     return:
    """
    raise NotImplementedError




def run():
    """
    Simple client runability tests.
    """
    channel = grpc.insecure_channel('localhost:50051')
    stub = dist_bank_pb2_grpc.DistBankStub(channel)

    print("Naive test cases:\n")

    print("-------------- LookupAccount --------------")
    bank_lookup_account(stub, dist_bank_pb2.LookupRequest(account_id="5a221afc35b38f9a0ba44b2c"))


    print("-------------- Save --------------")
    bank_withdraw_moneye(stub, dist_bank_pb2.WithdrawRequest(account_id="5a221afc35b38f9a0ba44b2c"),
                                                             with_amount=100.0)

    print("-------------- Withdraw --------------")
    bank_save_money(stub, dist_bank_pb2.SaveRequest(account_id="5a221afc35b38f9a0ba44b2c"),
                                                    save_amount=100.0)



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