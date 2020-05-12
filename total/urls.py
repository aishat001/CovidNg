from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('confirmed', views.ConfirmedApi)
router.register('active', views.ActiveApi)
router.register('discharged', views.DischargedApi)
router.register('death', views.DeathApi)
router.register('sample', views.SampleApi)
router.register('', views.TotalApi)


urlpatterns = [
	path('total/', include(router.urls)),
	path('total/latest', views.total_latest),
	path('total/delete',views.total_delete, name='delete_total'),
	path('login', views.LoginPage, name='login'),
]