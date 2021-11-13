from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('facility', views.facility_list, name="facilities"),
    path('manufacturers', views.manufacturer_list, name="manufacturers"),

    path('vaccines', views.vaccine_list, name="vaccines"),  
    path('vaccines/<int:pk>', views.vaccine_detail, name="vaccine_detail"),

    path('vaccinations', views.vaccination_list, name="vaccinations"),
    path('vaccinations/<int:pk>', views.vaccination_detail, name="vaccination_detail"),

    path('facility_activation/<int:pk>', views.facility_activation, name="facility_activation"),
    path('manufacturer_activation/<int:pk>', views.manufacturer_activation, name="manufacturer_activation"),
    path('vaccine_activation/<int:pk>', views.vaccine_activation, name="vaccine_activation"),   

]
