from django.urls import path, include
from . import views
from rest_framework import routers
from .views import AllRoutes


router = routers.DefaultRouter()
router.register('routes', AllRoutes)


urlpatterns = [
	path('', views.home, name='home'),
	path('', include(router.urls))
]