from django.db import models

class Subscribers(models.Model):

    email = models.CharField(max_length=100, blank = False, help_text='Email adress')
    full_name = models.CharField (max_length=100, blank = False, help_text='First and last name')

    def __str__(self):
        return self.full_name


# Create your models here.
