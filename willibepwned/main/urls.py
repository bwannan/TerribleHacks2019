from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('captcha', views.captcha.as_view(), name='captcha')
]
