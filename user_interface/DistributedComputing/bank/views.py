from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class SearchAccountView(View):
    def get(self, request):


        id = 11
        balance = 500
        return render(request, 'index.html', {'id': id, 'balance': balance})

    def post(self, request):

        if request.POST.get('type', '') == 'search':
            id = request.POST.get("id", 0)

            balance = 100

            # do search by user id
            return HttpResponse('{"status": "success","balance": balance}',
                                content_type="application/json")

        if request.POST.get('type', '') == 'save':
            id = request.POST.get("id", 0)
            amount = request.POST.get('amount', 0)

            balance = 200

            return HttpResponse('{"status": "success","balance": balance}',
                                content_type="application/json")

        if request.POST.get('type', '') == 'withdraw':
            id = request.POST.get("id", 0)
            amount = request.POST.get('amount', 0)

            balance = 300

            return HttpResponse('{"status": "success","balance": balance}',
                                content_type="application/json")

        return HttpResponse('{"status": "fail"}',
                            content_type="application/json")

