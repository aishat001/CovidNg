from django.shortcuts import render
from rest_framework import viewsets
from .models import Covid
from .serializer import StateSerializer
from django.http import HttpResponse

# Create your views here.


class StateListView(viewsets.ModelViewSet):
	queryset = Covid.objects.all()
	serializer_class = StateSerializer
	lookup_field = 'states_affected'
	http_method_names = ['get']


# class StateDeleteView(generics.RetrieveDestroyAPIView):
# 	queryset = Covid.objects.all()
# 	serializer_class = StateSerializer
def delete(request):
	queryset = Covid.objects.all()
	
	try:
		queryset.delete()
	
		return HttpResponse('All item deleted successfully ')
	except Exception as e:
		print(e)

	return HttpResponse('%s' %e)


def latest(request):
	import requests
	from bs4 import BeautifulSoup
	

	tab = []
	#url = 'covid2.html'
	url = requests.get('https://covid19.ncdc.gov.ng/')
	soup = BeautifulSoup(url.content, 'html.parser')
	custom1 = soup.find(class_ = "table-responsive")
	data = custom1.find('tbody')
	d2 = data.find_all('td')
	count = 0

	for item in d2:
		tab.append(item.text.strip('\n').strip(' '))
	while count != len(tab):
		# try:
		states_affected = tab[count ]
		lab_confirmed = tab[count + 1]
		admitted = tab[count + 2]
		discharged = tab[count + 3]
		death = tab[count + 4]
			
			
		# except Exception as e:
		# 	print(e)
		count += 5

	# for count in range(-1, 175, 4):
	# 	try:
	# 		states_affected = tab[count + 1]
	# 		lab_confirmed = tab[count + 2]
	# 		admitted = tab[count + 3]
	# 		discharged = tab[count + 4]
	# 		death = tab[count + 5]

	# 	except Exception as e:
	# 		pass
		state = Covid()
		state.states_affected = states_affected
		state.lab_confirmed = lab_confirmed
		state.admitted = admitted
		state.discharged = discharged
		state.death = death

		state.save()
	return HttpResponse('Latest Data Fetched')
