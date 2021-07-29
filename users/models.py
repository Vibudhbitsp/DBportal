from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
from django.urls import reverse

sex_choices = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Rather Not Say'),]
qualifier_choices = [('dber','dber'),('staff','staff')]
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    uid = models.IntegerField()
    name = models.CharField(max_length = 20)
    dob = models.DateField(default = timezone.now)
    gender = models.CharField(max_length = 6, choices = sex_choices, default = 1)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    mail = models.EmailField(null=True)
    qualifier = models.CharField(max_length=10,choices=qualifier_choices,default='staff')  #1 means staff

    def get_absolute_url(self):
        return reverse('send_mail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} Profile'




