from django.db import models
from django.contrib.auth.models import User

class customFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    gender_choices=(
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Prefers not to say'),
    )

    birthdate=models.DateField()
    gender=models.IntegerField(choices=gender_choices)
    # phoneNumber=models.IntegerField() 

    def __str__(self):
        return f'{self.user.username}'