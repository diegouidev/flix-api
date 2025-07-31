from django.db import models


NATIONALITIES = [
    ('American', 'American'),
    ('British', 'British'),
    ('Brazilian', 'Brazilian'),
    ('Canadian', 'Canadian'),
    ('Australian', 'Australian'),
    ('Other', 'Other'),
]

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITIES, blank=True, null=True)


    def __str__(self):
        return self.name