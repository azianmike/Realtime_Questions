from django.http import HttpResponse
# Create your views here.

from .models import User

def index(request):
    test = User.objects.create(_id="testUser", password="testPassword")    
    return HttpResponse("registered")


