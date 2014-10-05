# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Don't dare here")

def aview(request):
    return render(request,'test.html')

def cross_req(request):
    return HttpResponse("cross ok")