from django.db import models

class User(models.Model):

    gender_choices=(
        (0, 'male'),
        (1, 'female'),
        (2, 'prefers not to say'),
    )

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email=models.EmailField(max_length=254, unique=True)
    # phoneNumber=models.IntegerField() 
    birthdate=models.DateField()
    gender=models.IntegerField(choices=gender_choices)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'