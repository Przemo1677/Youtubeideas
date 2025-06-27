from django.shortcuts import render
from .models import Idea, Vote
from rest_framework import viewsets
from .serializer import IdeaSerializer, VoteSerializer

# Create your views here.

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    
    
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer