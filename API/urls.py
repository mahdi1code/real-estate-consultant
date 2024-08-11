from django.urls import path,include
from rest_framework import routers
from .views import Userviewset
from django.contrib.auth.models import User

roters=routers.DefaultRouter()
roters.register(r"User",Userviewset)

urlpatterns = [
    path('',include(roters.urls))
]
