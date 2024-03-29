from json import dumps
from register.models import User

__author__ = 'michaell'


def loginUser(request):
    '''
    Logs in a user if exists and return JSON object to return back to user.
    Note that if successfully logged in, return object will have an objectID for the user

    :param request: HTTP Request params/body/etc
    :return: return a JSON object with status on fail/success, if success, will have objectID for logged in user
    '''

    # get post PARAMS
    emailPost = request.POST.get("email", "")
    passwordPost = request.POST.get("password", "")

    #try catch to see if user exists
    return loginWithEmailAndName(emailPost, passwordPost)


def loginWithEmailAndName(emailPost, passwordPost):
    '''

    :param emailPost:
    :param passwordPost:
    :return:
    '''
    returnDict = {}
    returnDict['success'] = -1

    try:
        checkForUser = User.objects.get(email=emailPost, password=passwordPost)
        if checkForUser.activated == False:
            returnDict['success'] = -3
            returnDict['message'] = 'Please activate your email'
            return returnDict
        returnDict['success'] = 1
        returnDict['objectID'] = str(checkForUser.id)
        return returnDict
    except User.DoesNotExist:
        returnDict['success'] = 0
        returnDict['message'] = 'Email does not exist or password is not correct'
        return returnDict


def checkObjectID(request):
    returnDict = {}
    returnDict['success'] = -1
    objectID = request.POST.get("objectID", "")
    try:
        checkForUser = User.objects.get(id=objectID)
        returnDict['success'] = 1
        returnDict['message'] = 'objectID exists!'
        returnDict['email'] = checkForUser.email

        return returnDict

    except User.DoesNotExist:
        returnDict['success'] = 0
        returnDict['message'] = 'objectID does not exist'
        return returnDict