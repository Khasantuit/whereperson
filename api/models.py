from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name


class Quarter(models.Model):
    name = models.CharField(max_length=150)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='quarters')

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='people')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='people')
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, null=True, related_name='people')
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
         return f"{self.first_name} {self.last_name}"
