from .models import Routes
from rest_framework import serializers

class AllRoutesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routes
		fields = ('name', 'description', 'path',)