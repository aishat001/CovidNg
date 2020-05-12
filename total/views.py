from django.shortcuts import render, redirect
from .models import Total
from .serializer import TotalActiveSerializer, TotalConfirmedSerializer,TotalDischargedSerializer, TotalDeathSerializer, TotalSampleSerializer, TotalSerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
class TotalApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalConfirmedSerializer
	http_method_names = ['get']


class ActiveApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalActiveSerializer
	http_method_names = ['get']


class DischargedApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalDischargedSerializer
	http_method_names = ['get']


class DeathApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalDeathSerializer
	http_method_names = ['get']

class ConfirmedApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalConfirmedSerializer
	http_method_names = ['get']

class SampleApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalSampleSerializer
	http_method_names = ['get']


class TotalApi(viewsets.ModelViewSet):
	queryset = Total.objects.all()
	serializer_class = TotalSerializer
	http_method_names = ['get']


def total_latest(request):
	from bs4 import BeautifulSoup
	import requests
	tab = []
	#url = 'covid2.html'
	url = requests.get('https://covid19.ncdc.gov.ng/')
	soup = BeautifulSoup(url.content, 'html.parser')
	#soup = BeautifulSoup(open(url), 'html.parser')
	custom1 = soup.find(class_ = 'text-right text-white')
	# tr = custom1.find_all('tr')
	# print(tr.text)

	#confirmed_cases = custom1.text
	active_cases = soup.find_all('h2')
	
	sample = active_cases[0].text[1:]
	confirmed = active_cases[1].text 
	active = active_cases[2].text
	discharged = active_cases[3].text
	death = active_cases[4].text 


	# tab.append({
	# 	'Samples Tested': active_cases[0].text[2:],
	# 	'confirmed_cases': active_cases[1].text,
	# 	'Active Cases': active_cases[2].text,
	# 	'Discharged Cases': active_cases[3].text,
	# 	'Death': active_cases[4].text})

	# for item in tab:
	# 	for k, v in item.items():
	# 		print(k, ': ', v)
	try:
		total = Total()
		total.sample = sample
		total.confirmed = confirmed
		total.active = active
		total.discharged = discharged
		total.death = death 

		total.save()
	except Exception as e:
		print(e)

	return HttpResponse('Latest Total Data fetched')


def total_delete(request):
	queryset = Total.objects.all()
	print(queryset)
	try:
		queryset.delete()
	
		return HttpResponse('All item deleted successfully ')
	except Exception as e:
		print(e)

	return HttpResponse('%s' %e)

def LoginPage(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('list-total')

		else:
			messages.info(request, 'Parameters provided not correct')
  
	return render(request, 'login.html', {})


def RegisterPage(request):

	return render(request, 'logout.html', {})