from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('facility', views.facility_list, name="facilities"),
    path('manufacturers', views.manufacturer_list, name="manufacturers"),
    path('vaccines', views.vaccine_list, name="vaccines"),    
    path('vaccinations', views.vaccination_list, name="vaccinations"),
    path('vaccinations/<int:pk>', views.vaccination_detail, name="vaccination_detail"),

    path('next_vaccinations', views.next_vaccination_list, name="next_vaccinations"),
    path('next_vaccinations/<int:pk>', views.next_vaccination_detail, name="next_vaccination"),    

    # path('facility_activation/<int:pk>', views.facility_activation, name="facility_activation"),
    # path('manufacturer_activation/<int:pk>', views.manufacturer_activation, name="manufacturer_activation"),
    # path('vaccine_activation/<int:pk>', views.vaccine_activation, name="vaccine_activation"),   

]
