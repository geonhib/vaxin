from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import UserForm
from accounts.models import Message
from django.contrib import messages
from jab.models import Vaccination, Vaccine


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "account/base.html")


def profile(request):
    # user = User.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)

    edit_user = UserForm(request.POST, request.FILES, instance=user)
    if edit_user.is_valid():
        instance = edit_user.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'User updated succesfully!')
        return redirect('profile')

    reminders = Message.objects.filter(user=request.user, category="reminder")[:5]
    vaccinations = Vaccination.objects.filter(patient=request.user)
   
    context = {
        "edit_user": edit_user,
        "reminders": reminders, 
        "vaccinations": vaccinations,
    }
    return render(request, "account/profile.html", context)


def dashboard(request):
    vaccines = Vaccine.objects.count()
    vaccinations = Vaccination.objects.count()
    reminders = Message.objects.filter(category="reminder").count()
    users = User.objects.all()
    female = users.filter(gender="female").count()
    male = users.filter(gender="male").count()

    context = {
        "reminders": reminders,
        "vaccinations": vaccinations,
        "vaccines": vaccines,
        "reminders": reminders, 
        "users": users.count(),
        "female": female,
        "male": male,
    }
    return render(request, "dashboard.html", context)    


def reminders(request):
    reminders = Message.objects.filter(user=request.user, category="reminder")
    context = {
        "reminders": reminders, 
    }
    return render(request, "messages/reminders.html", context)
