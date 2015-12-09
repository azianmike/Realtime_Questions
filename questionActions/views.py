from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from questionActions.models import Question
from register.models import User
from django.http import HttpResponse
from json import dumps
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
    timeSubmittedPOST = request.POST.get("timeSubmitted", "")
    #time (in hrs) that the question should be active for
    expirationTimePOST = request.POST.get("expirationTime", 0)
    #question has to be active by default, right?
    isActivePOST = True
    #the bid amount that the user who submitted wants to BET
    submitUserBidPOST = request.POST.get("submitUserBid", 0)
    #max bid at the start has to be the submit user bid right? or 0 to signify no one has bidded
    maxBidPOST = 0


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
    returnDict = {}
    returnDict['success'] = 1
    returnDict['message'] = "Question successfully submitted!"
    return returnDict

