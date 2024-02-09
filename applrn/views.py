from django.shortcuts import render
from datetime import datetime

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello, world!!")

def index(request):
    return HttpResponse(f"time: {datetime.now()}")

