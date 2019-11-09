from django.urls import path

from . import views

urlpatterns = [
        path('create/', views.create),
        path('email/', views.send_email),
        path('numexposed/', views.numexposed),
        path('randomexpose/', views.randomexpose),
        path('giveimages/',views.giveimages),
]

