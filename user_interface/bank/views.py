#encoding: utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
import grpc
from utils import dist_bank_client, dist_bank_pb2_grpc, dist_bank_pb2


class IndexView(View):
    def get(self, request):

        id = 'Null'
        balance = 0
        return render(request, 'index.html', {'id': id, 'balance': balance})

    def post(self, request):

        type_ = request.POST.get('type', '')
        id = request.POST.get("id", 0)
        amount = request.POST.get('amount', 0)

        #  搜索用户
        if type_ == 'search':
            # invoke the function here

            channel = grpc.insecure_channel('localhost:50051')
            stub = dist_bank_pb2_grpc.DistBankStub(channel)

            result = dist_bank_client.bank_lookup_account(stub, dist_bank_pb2.LookUpRequest(uid=id))
            balance = result.balance

            dicts = {"status": "success", "balance": balance, "type": type_, 'id': id}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        # 存钱
        if type_ == 'save':
            amount = request.POST.get('amount', 0)

            # invoke the function here, and use balance to receive the result

            channel = grpc.insecure_channel('localhost:50051')
            stub = dist_bank_pb2_grpc.DistBankStub(channel)

            result = dist_bank_client.bank_save_money(stub, dist_bank_pb2.SaveRequest(uid=id,
                                                                                      save_amount=float(amount)))

            balance = result.balance

            dicts = {"status": "success", "balance": balance, "type": type_}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        # 提现
        if type_ == 'withdraw':
            amount = request.POST.get('amount', 0)

            # invoke the function here, and use balance to receive the result
            channel = grpc.insecure_channel('localhost:50051')
            stub = dist_bank_pb2_grpc.DistBankStub(channel)

            result = dist_bank_client.bank_withdraw_money(stub, dist_bank_pb2.WithdrawRequest(uid=id,
                                                                                          with_amount=float(amount)))

            balance = result.balance

            dicts = {"status": "success", "balance": balance, "type": type_}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        return HttpResponse('{"status": "fail"}',
                            content_type="application/json")


