from django.db import models

# Create your models here.


class Employee(models.Model):
    firstname = models.CharField(max_length= 100)
    secondname = models.CharField(max_length= 100)
    employer_id = models.IntegerField()

    def __str__(self):
        return self.firstname 