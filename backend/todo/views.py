import os

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import TodoSerializer, RequestSerializer, ArticleSerializer, ReturnsSerializer
from .models import Krarecords, Jobrequest, Returns
from .models import Jobrequest,Article
from rest_framework.generics import RetrieveAPIView
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, "build/index.html")

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Krarecords.objects.all()

class ReturnsView(viewsets.ModelViewSet):
    serializer_class = ReturnsSerializer
    queryset = Returns.objects.all()

class TitleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-id')[:8]

class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Jobrequest.objects.all()

class NewjobsView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Jobrequest.objects.filter(datecompleted__isnull=True)

class CjobsView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Jobrequest.objects.filter(datecompleted__isnull=False)


class CkraView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Krarecords.objects.filter(datecompleted__isnull=False)

class NewkraView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Krarecords.objects.filter(datecompleted__isnull=True)

class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-id')
    

class PostDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class Post(RetrieveAPIView):
    def getnumber_of_records(self):
        new_request=Krarecords.objects.filter(datecompleted__isnull=True).count() +Jobrequest.objects.filter(datecompleted__isnull=True).count()
        complete_requests=Krarecords.objects.filter(datecompleted__isnull=False).count() +Jobrequest.objects.filter(datecompleted__isnull=False).count()
        total_articles=Article.objects.all()
        data = {
            'newrequest': new_request,
            'completerequests':complete_requests,
            'totalarticles':total_articles
        }
        return JsonResponse(data)

