from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('models', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('reminders', views.reminders, name='reminders'),

]
