from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from re import match
from django.template.defaulttags import csrf_token
from json import dumps
import datetime
from hashlib import sha224
from .models import User


def checkValidEmail(email):
    pattern = r"(^[^@]+@[^@]+\.[^@]+)"
    return bool(match(pattern,email))

@csrf_exempt
def index(request):
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")
    returnDict = {}

    try:
        checkOld = User.objects.get(_id=emailPost)
        returnDict['success']=-1
        returnDict['message']="Email is already registered!"
        return HttpResponse(dumps(returnDict))
    except User.DoesNotExist:
        if not checkValidEmail(emailPost):
            returnDict['success'] = -1
            returnDict['message']='Invalid email address'
            return HttpResponse(dumps(returnDict))
        #f='%Y-%m-%d'
        #now = datetime.datetime.now()
        #mysqlTime = now.strftime(f)
        #userToAdd = User.objects.create(_id=emailPost, password=passwordPost, joinDate=mysqlTime)
        userToAdd = User(_id=emailPost, password=passwordPost, activated=False)
        userToAdd.save()
        returnDict['success']= 1
        returnDict['message'] = "Registered! Check your email to activate your account"
        return HttpResponse(dumps(returnDict))                



