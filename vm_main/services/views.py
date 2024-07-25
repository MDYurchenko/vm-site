from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contract


def hello_world(request):
    return HttpResponse("Hello, World!")


def get_contract_short_info(request):
    simple_answer = {
        'status': 200,
        'answer': 'it is good'
    }
    return JsonResponse(simple_answer)


def get_contracts_list(request):
    contracts = Contract.objects.all()# models.Manager???
    d = [{'number': entry.number, 'client': entry.client.organization_name, 'service': entry.service.name} for entry in contracts]
    data = {
        'contracts': [d]
    }
    return JsonResponse(data)
