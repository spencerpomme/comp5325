# encoding: utf-8
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
        id = request.POST.get("id", "")
        amount = request.POST.get('amount', 0)

        # 检查是否为数字
        try:
            amount = float(amount)
        except:
            return HttpResponse('{"status":"fail", "type":"ValueError"}', content_type="application/json")

        #  搜索用户
        if type_ == 'search':

            result = dist_bank_client.look_up_wrapper(dist_bank_pb2.LookUpRequest(uid=id))

            # 该ID 不存在
            if result.uid == "0":
                return HttpResponse('{"status":"fail", "type":"NoID"}',
                                    content_type="application/json")

            balance = result.balance
            uid_exist = True
            dicts = {"status": "success", "balance": balance, "type": type_, 'id': id}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        # 存钱
        if type_ == 'save':

            result = dist_bank_client.look_up_wrapper(dist_bank_pb2.LookUpRequest(uid=id))

            # 该ID 不存在
            if result.uid == "0":
                return HttpResponse('{"status":"fail", "type":"NoID"}',
                                    content_type="application/json")

            amount = request.POST.get('amount', 0)

            result = dist_bank_client.save_wrapper(dist_bank_pb2.SaveRequest(uid=id,
                                                                             save_amount=float(amount)))

            print(result.index)

            balance = result.balance

            dicts = {"status": "success", "balance": balance, "type": type_}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        # 提现
        if type_ == 'withdraw':

            result = dist_bank_client.look_up_wrapper(dist_bank_pb2.LookUpRequest(uid=id))

            # 该ID 不存在
            if result.uid == "0":
                return HttpResponse('{"status":"fail", "type":"NoID"}',
                                    content_type="application/json")

            amount = request.POST.get('amount', 0)

            result = dist_bank_client.withdraw_wrapper(gdist_bank_pb2.WithdrawRequest(uid=id,
                                                                                      with_amount=float(amount)))

            # 余额不足
            if result.index == -1:
                return HttpResponse('{"status":"fail", "type":"NoEnoughMoney"}',
                                    content_type="application/json")

            balance = result.balance

            dicts = {"status": "success", "balance": balance, "type": type_}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        return HttpResponse('{"status": "fail"}',
                            content_type="application/json")
