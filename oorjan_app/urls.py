from django.conf.urls import url
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'solar_data', SolarDataViewSet)

# from django.conf.urls import url

# from . import views

urlpatterns = [
    url(r'solar_data', views.solar_data_request),

]

# urlpatterns = router.urls