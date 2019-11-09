from django.contrib import admin
from django.urls import include, path
from .views import Index

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="Index"),
]
