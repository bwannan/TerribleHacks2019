from django.shortcuts import render
from main.models import smuck
from django.http import JsonResponse 
# Create your views here.
def randomexpose(request):
    a = smuck.objects.order_by('?').first()    

    return a

def numexposed(request):
    a = smuck.objects.latest('id').id
    return JsonResponse({"numberofpeopleextoreted":a})

def create(request):

    tosave = smuck.objects.create(email='123@email.com', username='abc', password='bb')
    return JsonResponse({"result":"created"})
   

def giveimages(request):

