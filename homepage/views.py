from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Routes
from .serializer import AllRoutesSerializer
# Create your views here.


def home(request):
	return render(request, 'home.html')

class AllRoutes(viewsets.ModelViewSet):
	queryset = Routes.objects.all()
	serializer_class = AllRoutesSerializer
	http_method_names = ['get']