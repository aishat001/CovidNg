from rest_framework import serializers
from .models import Covid


class StateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Covid
		fields = ('__all__')
		extra_kwargs = {'url': {'lookup_field': 'states_affected'}}

