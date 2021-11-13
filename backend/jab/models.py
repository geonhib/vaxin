from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL

# Create your models here.
CENTER_LEVEL = (
    ('HC I', 'HC I'),
    ('HC II', 'HC II'),
    ('HC III', 'HC III'),
    ('HC IV', 'HC IV'),
    ('Regional Referal Hospital', 'Regional Referal Hospital'),
    ('National Hospital', 'National Hospital'),
    ('Private Hospital', 'Private Hospital'),   
        )
class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    center_level = models.CharField(max_length=60, choices=CENTER_LEVEL, default='Private Hospital', null=True)
    contact = models.EmailField()
    active  = models.BooleanField(default=False)

    class Meta :
       ordering = ['-name']

    def __str__(self):
        return f"{self.name}" 

    
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=False)
    contact = models.EmailField()
    approved  = models.BooleanField(default=False)

    class Meta :
       ordering = ['-name']

    def __str__(self):
        return f"{self.name}" 


class Vaccine(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)    
    doses = models.IntegerField(default=1)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    approved  = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now=True)

    class Meta :
       ordering = ['-name']

    def supply_diff(self):
        """Difference btn initial order and current supply."""
        x=self.order.quantity - self.quantity
        return x 

    def __str__(self):
        return f"{self.name}"


class Batch(models.Model):
    drug = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    batch = models.CharField(primary_key=True, max_length=50)        
    serial = models.CharField(max_length=50, null=True, blank=True)     
    expiry = models.DateField(auto_now_add=False, auto_now=False)
    approved  = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now=True)

    class Meta :
       ordering = ['-expiry']

    def __str__(self):
        return f"{self.drug} - {self.batch}"


DOSAGE_CHOICES = (
    ("soon", "soon"),
    ("taken", "taken"),
    ("missed", "missed")
)
class Vaccination(models.Model):   
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vaccinatee')
    drug = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    jabbed_on = models.DateField(auto_now_add=False, auto_now=False)
    jabbed_at = models.ForeignKey(Facility, on_delete=models.CASCADE)
    jabbed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vaccinator')
    dose = models.CharField(max_length=30, choices=DOSAGE_CHOICES, default="taken")
    next_dose = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    class Meta :
       ordering = ['-jabbed_on']

#     def remind(self):
#         tomorrow = date.today() + timedelta(days=1)
#         yesterday = date.today() - timedelta(days=1)
#         patient_email=self.patient.user.email
#         patient_tel = self.patient.telephone
#         prep_message = f"Hi {self.patient}, please prepare for your next {self.drug.name} dose tomorrow."
#         late_message = f"Hi {self.patient}, you missed your {self.drug.name} dose yesterday, please look for a clinic and take your dose ."

#         if self.next_dose == tomorrow:
#             pass
#             send_mail(subject='Vaccination Reminder', message=prep_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[patient_email])
#             Message.objects.create(content=prep_message, timestamp=datetime.now, profile=self.patient)
#             sms.send(prep_message, [patient_tel], callback=on_finish)     
#         elif self.next_dose == yesterday:
#             send_mail(subject='Vaccination Reminder', message=late_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[patient_email])  
#             Message.objects.create(content=late_message, timestamp=datetime.now, profile=self.patient)   
#             sms.send(late_message, [patient_tel], callback=on_finish)     
#         else:
#             return "Vaccination date soon, stay safe"

#     def doses_left(self):
#         doses_rem = self.drug.doses - 1
#         return doses_rem

#     def compare_dates(self):
#         today = datetime.now().date()
#         if self.next_dose < today:
#             missed_by = today - self.next_dose
#             return f" missed by {missed_by}"
#         else:
#             ctd = self.next_dose - today
#             return f"{ctd}  to go!"              

#     # TODO: recommend jab locations
    def __str__(self):
        return f"{self.drug}"  


class NextVaccination(models.Model):   
    drug = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    init_vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE)
    jabbed_on = models.DateField(auto_now_add=False, auto_now=False)
    jabbed_at = models.ForeignKey(Facility, on_delete=models.CASCADE)
    jabbed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nextvacc_medic')
    dose = models.BooleanField(default=False)
    next_dose = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    # def remind(self):
    #     tomorrow = date.today() + timedelta(days=1)
    #     yesterday = date.today() - timedelta(days=1)
    #     patient_email=self.patient.user.email
    #     patient_tel = self.patient.telephone
    #     prep_message = f"Hi {self.patient}, please prepare for your next {self.drug.name} dose tomorrow."
    #     late_message = f"Hi {self.patient}, you missed your {self.drug.name} dose yesterday, please look for a clinic and take your dose ."

    #     if self.next_dose == tomorrow:
    #         send_mail(subject='Vaccination Reminder', message=prep_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[patient_email])
    #         Message.objects.create(content=prep_message, timestamp=datetime.now, profile=self.patient)
    #         sms.send(prep_message, [patient_tel], callback=on_finish)    
    #     elif self.next_dose == yesterday:
    #         send_mail(subject='Vaccination Reminder', message=late_message, from_email=settings.EMAIL_HOST_USER, recipient_list=[patient_email])  
    #         Message.objects.create(content=late_message, timestamp=datetime.now, profile=self.patient)   
    #         sms.send(late_message, [patient_tel], callback=on_finish)     
    #     else:
    #         return "Appt soon, stay safe"

    # def doses_left(self):
    #     doses_rem = self.init_vaccination.drug.doses - 1
    #     # start = self.init_vaccination.drug.doses 
    #     # end = 0 
    #     # step= -1  
    #     # for x in range(start, end, step):
    #     #     print(x)
    #     #     return x
    #     return doses_rem

    # def compare_dates(self):
    #     today = datetime.now().date()
    #     if self.next_dose < today:
    #         missed_by = today - self.next_dose
    #         return f" missed by {missed_by}"
    #     else:
    #         ctd = self.next_dose - today
    #         return f"{ctd} to go!" 
 

    # TODO: recommend jab locations
    def __str__(self):
        return f"{self.drug}"


