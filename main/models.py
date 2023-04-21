from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=15)
    birthdate = models.DateField()

    def __str__(self):
        return self.name
