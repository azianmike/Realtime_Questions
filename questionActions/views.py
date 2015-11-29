from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from register.models import User
from django.http import HttpResponse
from json import dumps
# Create your views here.

@csrf_exempt
def index(request):
    returnDict = {}

    return HttpResponse(dumps(returnDict))
    
