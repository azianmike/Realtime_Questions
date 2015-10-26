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
    returnDict['success'] = -1
    
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")
    
    try:
        checkForUser = User.objects.get(_id=emailPost, password=passwordPost)
        if checkForUser.activated == False:
            returnDict['success'] = -3
            returnDict['message'] = 'Please activate your email'
            return HttpResponse(dumps(returnDict))
        returnDict['success'] = 1
        request.session['has_loggedin'] = True
        request.session['email'] = emailPost
        return HttpResponse(dumps(returnDict))
    except User.DoesNotExist:
        returnDict['success'] = 0
        returnDict['message'] = 'Email does not exist or password is not correct'
        return HttpResponse(dumps(returnDict))

    return HttpResponse('loginSuccess')
