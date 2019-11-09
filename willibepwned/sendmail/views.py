from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def index(request):
    pass
    # render(request, "")

# subject = "YOU'VE BEEN L33T HAXXED N00B!!"
# message = "Hello, we are elite hacker team. You system has been comprimised. If you do not to us send 500 $ dollar, we will post you credential for everyone to see."

# def send_email(request):
#     password = request.POST.get('password', '')
#     from_email = request.POST.get('to_email', '')
#     if subject and message and from_email:
#          try:
#             send_mail(subject, message, ['l33thaxx0rs@supersecretsite.com'], to_email)
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')

