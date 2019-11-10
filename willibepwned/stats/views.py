from django.shortcuts import render
from main.models import smuck
from django.http import JsonResponse 
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def randomexpose(request):
#    user_obj = smuck.objects.order_by('?').first()
    user_obj = smuck.objects.all()
    random_item = random.sample(list(user_obj),1)
    random_item = random.choice(user_obj)
    ret = {'username': random_item.username, 'password':random_item.password, 'email': random_item.email}
    return JsonResponse(ret);

def numexposed(request):
    user_obj = smuck.objects.latest('id').id
    return JsonResponse({"numberofpeopleextoreted":user_obj})

def create(request):

    _username = request.POST.get('username', '')
    _password = request.POST.get('password', '')
    _email = request.POST.get('email', '')

    tosave = smuck.objects.create(email=_email, username=_username, password=_password)
    return JsonResponse({"result":"created"})

def giveimages(request):
    pass

def send_email(request):
    #Option 1: Get random user object from database
    # user_obj = smuck.objects.all()
    # random_item = random.choice(user_obj)
    # username = random_item.username
    # password = random_item.password
    # to_email = random_item.email

#    Option 2: Use current user object
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    to_email = request.POST.get('email', '')

    subject = "YOU'VE BEEN HAXXED N00B!!"
    message1 = "Hello, we are elite l33t hacker team. You system has been comprimised. \
    If you do not to us send 5,000,000$ million dollar, we will post you credential for everyone to see. \
    \r You do not trust great hacker skills? Here is proof: \
    \r you username:" + username
    message2 = "\r you password: " + password
    message3 = "\r do Not worry, if the 5,0000,000 is send, we will be deleting all information. \
    \r DO NOT try to contact the police:we monitoring all your account and we release the information \
    if police are contacted." + "\r thank you for cooperation.\r L33t Haxx0rs"
    full_message = message1 + message2 + message3
    from_email = [settings.EMAIL_HOST_USER]
    if to_email and username and password:
        send_mail(subject, full_message, from_email, [to_email])
#   return HttpResponseRedirect('/main/confirm')
    return HttpResponse()
