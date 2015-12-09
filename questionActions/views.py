from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from questionActions.models import Question
from register.models import User
from django.http import HttpResponse
from json import dumps
from datetime import datetime
# Create your views here.

@csrf_exempt
def submitQuestion(request):
    returnDict = {}

    return HttpResponse(dumps(submitQuestionHelper(request)))
    

def submitQuestionHelper(request):
    #user who submitted
    userIDPOST = request.POST.get("userID", "")
    #text of the question submitted
    questionTextPOST = request.POST.get("questionText", "")
    #number of answers, defaults to 0
    numOfAnswersPOST = request.POST.get("numOfAnswers", 0)
    #array of all the possible answer choices that someone could answer with
    arrayOfAnswersPOST = request.POST.get("arrayOfAnswers", "{}")
    #time submitted, need to get from due to locale info and network inconsistencies
    #example is Jun 1 2005  1:33PM
    #http://stackoverflow.com/questions/466345/converting-string-into-datetime
    try:
        timeSubmittedPOST = request.POST.get("timeSubmitted", "")
        timeSubmittedPOST = datetime.strptime(timeSubmittedPOST, '%b %d %Y %I:%M%p')
        #time (in hrs) that the question should be active for
        expirationTimePOST = request.POST.get("expirationTime", 0)
        expirationTimePOST = datetime.strptime(expirationTimePOST, '%b %d %Y %I:%M%p')
    except:
        return makeReturnDict(-1, "timeSubmitted and expirationTime are not correctly formatted")
    #question has to be active by default, right?
    isActivePOST = True
    #the bid amount that the user who submitted wants to BET
    submitUserBidPOST = request.POST.get("submitUserBid", 0)
    #max bid at the start has to be the submit user bid right? or 0 to signify no one has bidded
    maxBidPOST = 0

    if questionTextPOST[-1] != '?':
        questionTextPOST += '?'

    #TODO Error validation on these things
    questionToSubmit = Question(submitUserID = userIDPOST,
                                questionText = questionTextPOST,
                                numOfAnswers = numOfAnswersPOST,
                                arrayOfAnswers = arrayOfAnswersPOST,
                                timeSubmitted = timeSubmittedPOST,
                                expirationTime = expirationTimePOST,
                                isActive = isActivePOST,
                                submitUserBid = submitUserBidPOST,
                                maxBid = maxBidPOST
    )
    questionToSubmit.save()

    return makeReturnDict(1, "Question successfully submitted!")

def makeReturnDict(successStatus, message):
    returnDict = {}
    returnDict['success'] = successStatus
    returnDict['message'] = message

    return returnDict
