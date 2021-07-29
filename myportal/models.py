from django.contrib.auth.models import User
from django.db import models




from django.utils import timezone

from users.models import Profile

class Portal(models.Model):

    staff = models.ForeignKey(Profile, on_delete = models.CASCADE,null=True)
    file_name = models.CharField(max_length=20)
    doc = models.FileField(upload_to='media')
    up_date = models.DateField(default = timezone.now)

    def __str__(self):
        return f'{self.file_name}'

    