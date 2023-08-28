from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Empoyee
# Create your views here.

def employeeView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 1000000
    }

    data = Empoyee.objects.all()
    response ={'employees': list(data.values('name', 'sal'))}
    return JsonResponse(response)