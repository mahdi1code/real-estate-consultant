from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serilizer import Userserilisers
# Create your views here.

class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserilisers
