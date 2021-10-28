from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate
from .models import Facility, Manufacturer, Vaccine, Vaccination
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import FacilityForm, ManufacturerForm, VaccineForm, VaccinationForm
# from account.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from accounts.forms import UserForm


@login_required(login_url='login') 
def facility_list(request):
    if request.user.is_superuser:
        facilities = Facility.objects.all()
    else:
        facilities = Facility.objects.filter(active=True)
    facility_count = facilities.count()

    create_form = FacilityForm(request.POST or None, request.FILES or None)
    if create_form.is_valid():
        instance = create_form.save(commit=False)
        instance.active = False
        instance.save()  
        messages.success(request, 'facility created successful')
        return redirect('facilities')
    context = {
        "create_form": create_form,
        "facilities": facilities,
        "facility_count": facility_count
    }
    return render(request, 'facility/list.html', context)  


@login_required(login_url='login') 
def manufacturer_list(request):
    if request.user.is_superuser:   
        manufacturers = Manufacturer.objects.all()
    else:
        manufacturers = Manufacturer.objects.filter(approved=True)
    manufacturer_count = manufacturers.count()
     
    create_form = ManufacturerForm(request.POST or None, request.FILES or None)
    if create_form.is_valid():
        instance = create_form.save(commit=False)
        instance.approved = False
        instance.save()                  
        messages.success(request, 'Drug manufacturer created successfully')
        return redirect('manufacturers')
    context = {
        "create_form": create_form,
        "manufacturers": manufacturers,
        "manufacturer_count": manufacturer_count
    }
    return render(request, 'manufacturer/list.html', context)  


@login_required(login_url='login') 
def vaccine_list(request):
    if request.user.is_superuser:   
        vaccines = Vaccine.objects.all()
    else:
        vaccines = Vaccine.objects.filter(approved=True)
    vaccine_count = vaccines.count()  
    
    create_form = VaccineForm(request.POST or None, request.FILES or None)
    if create_form.is_valid():
        instance = create_form.save(commit=False)
        instance.approved = False
        instance.save()                 
        messages.success(request, 'Vaccine registered successfully')
        return redirect('vaccines')

    context = {
        "create_form": create_form,
        "vaccines": vaccines,
        "vaccine_count": vaccine_count
    }
    return render(request, 'vaccine/list.html', context)  


@login_required(login_url='login') 
def vaccination_list(request):
    vaccinations = Vaccination.objects.all()
    # vaccination_count = vaccinations.count() 

    create_form = VaccinationForm(request.POST or None, request.FILES or None)
    if create_form.is_valid():
        instance = create_form.save(commit=False)
        instance.jabbed_by = request.user.profile
        instance.jabbed_on = datetime.date(datetime.now())
        instance.save()                
        messages.success(request, 'Vaccination registered successfully')
        return redirect('vaccinations')

    context = {
        "create_form": create_form,
        "vaccinations": vaccinations,
        # "vaccination_count": vaccination_count
    }
    return render(request, 'vaccination/list.html', context)  


@login_required(login_url='login') 
def vaccination_detail(request, pk): 
    vaccination = get_object_or_404(Vaccination, pk=pk) 
    user = User.objects.get(username=request.user.username)
    

    edit_profile = UserForm(request.POST, request.FILES, instance=user)
    if edit_profile.is_valid():
        edit_profile.save()
        messages.success(request, 'Profile updated succesfully!')

    # update 
    edit_form = VaccinationForm(request.POST or None, instance=vaccination)
    if edit_form.is_valid():
        edit_form.save()
        details = f"updated {vaccination}s details."
        messages.success(request, 'vaccination updated succesfully!')
        return redirect('vaccination_detail')

    
    # # next vaccination
    # nvacc_form = NextVaccinationForm(request.POST or None)
    # if nvacc_form.is_valid():
    #     instance = nvacc_form.save(commit=False)
    #     instance.init_vaccination = Vaccination.objects.get(pk=pk)
    #     instance.drug = vaccination.drug
    #     instance.jabbed_by = request.user.profile
    #     instance.jabbed_on = datetime.date(datetime.now())
    #     instance.save()
    #     details = f"updated {vaccination}s details."
    #     messages.success(request, 'vaccination updated succesfully!')
    #     return redirect('vaccination_detail', pk=pk)        

    # vey = NextVaccination.objects.filter(init_vaccination=vaccination)
    

    context = {
        "vaccination" : vaccination,
        "edit_form": edit_form,
        # "edit_profile": edit_profile,
        # "nvacc_form": nvacc_form,
        # "vey": vey,
    } 
    return render(request, 'vaccination/detail.html', context)  



@login_required(login_url='login') 
def next_vaccination_list(request): 
    pass

@login_required(login_url='login') 
def next_vaccination_detail(request, pk): 
    pass




@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='login') 
def facility_activation(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    grant_msg = f"facility approved"
    revoke_msg = f"facility revoked"    
    if facility.active == True:
        facility.active = False
        facility.save()
        messages.warning(request, revoke_msg)
    else:
        facility.active == False
        facility.active = True
        facility.save()    
        messages.success(request, grant_msg)
    return redirect('facilities') 


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='login') 
def manufacturer_activation(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    grant_msg = f"manufacturer approved"
    revoke_msg = f"manufacturer revoked"    
    if manufacturer.approved == True:
        manufacturer.approved = False
        manufacturer.save()
        messages.warning(request, revoke_msg)
    else:
        manufacturer.approved == False
        manufacturer.approved = True
        manufacturer.save()    
        messages.success(request, grant_msg)
    return redirect('manufacturers') 



@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='login') 
def manufacturer_activation(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    grant_msg = f"manufacturer approved"
    revoke_msg = f"manufacturer revoked"    
    if manufacturer.approved == True:
        manufacturer.approved = False
        manufacturer.save()
        messages.warning(request, revoke_msg)
    else:
        manufacturer.approved == False
        manufacturer.approved = True
        manufacturer.save()    
        messages.success(request, grant_msg)
    return redirect('manufacturers') 


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='login') 
def vaccine_activation(request, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    grant_msg = f"vaccine approved"
    revoke_msg = f"vaccine revoked"    
    if vaccine.approved == True:
        vaccine.approved = False
        vaccine.save()
        messages.warning(request, revoke_msg)
    else:
        vaccine.approved == False
        vaccine.approved = True
        vaccine.save()    
        messages.success(request, grant_msg)
    return redirect('vaccines') 