from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
User=settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    # add additional fields in here
    telephone = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# MESSAGE_CHOICES = (
#     ("information", "information"),
#     ("reminder", "reminder"),
# )
# STATUS_CHOICES = (
#     ("pending", "pending"),
#     ("resolved", "resolved"),
# )
# class Message(models.Model):
#     category = models.CharField(max_length=50, choices=MESSAGE_CHOICES, null=True)
#     # subject = models.CharField(max_length=100, null=True)
#     content = models.TextField(null=True, blank=False)
#     status = models.CharField(max_length=100, null=True, blank=True, choices=STATUS_CHOICES, default="pending")    
#     timestamp = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
#     user = models.ForeignKey(User, models.CASCADE)

#     def __str__(self):
#         return f"{self.content}" 

#     class Meta:
#         ordering = ('-timestamp',) 