from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class captcha(TemplateView):
    template_name='captcha.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context["images"] = getImages() 
        return context

def getImages():
    images = [["static/img/hot0.jpg", 0],
        ["static/img/hot0.jpg", 1],
        ["static/img/hot0.jpg", 2]]
    return images   