from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class captcha(TemplateView):
    template_name='captcha.html'