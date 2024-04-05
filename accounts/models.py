
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


class Client(User):
    COUNTRY_CHOICES = (('AU', 'Australia'), ('USA', 'USA'))
    CITY_CHOICES = (
        ('SYD', 'Sydney'), ('MEL', 'Melbourne'),
        ('NY', 'New York'), ('SFS', 'San Francisco'))
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Client'

    def __str__(self):
        return f'{self.username}'

    @admin.display(ordering='country',  description='Location',
                   empty_value='--')
    def location(self):
        return f'{self.city.name}, {self.country.name}'


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Cities'
