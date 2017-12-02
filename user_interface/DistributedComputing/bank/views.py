#encoding: utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json


class SearchAccountView(View):
    def get(self, request):

        id = 11
        balance = 500
        return render(request, 'index.html', {'id': id, 'balance': balance})

    def post(self, request):

        type_ = request.POST.get('type', '')

        #  搜索用户
        if type_ == 'search':
            id = request.POST.get("id", 0)
            balance = 100

            # invoke the function here

            dicts = {"status": "success", "balance": balance, "type": type_, 'id': id}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        # 存钱
        if type_ == 'save':
            id = request.POST.get("id", 0)
            amount = request.POST.get('amount', 0)

            balance = 200

            # invoke the function here, and use balance to receive the result

            dicts = {"status": "success", "balance": balance, "type": type_}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        # 提现
        if type_ == 'withdraw':
            id = request.POST.get("id", 0)
            amount = request.POST.get('amount', 0)

            balance = 300

            # invoke the function here, and use balance to receive the result

            dicts = {"status": "success", "balance": balance, "type": type_}

            return HttpResponse(json.dumps(dicts),
                                content_type="application/json")

        return HttpResponse('{"status": "fail"}',
                            content_type="application/json")

