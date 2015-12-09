from mongoengine import *

connect('realtimeQuestions_DB')

class Question(Document):
    questionText = StringField(required=True)
    numOfAnswers = IntField(required=True)
    arrayOfAnswers = StringField(required=True)
    submitUserID = ObjectIdField(required=True) #user objectID
    timeSubmitted = DateTimeField(required=True)
    expirationTime = DateTimeField(required=True)
    isActive = BooleanField(required=True)
    submitUserBid = IntField(required=True)
    maxBid = IntField(required=True)
    #category = ObjectIdField(required=True) #category ObjectID


