from django.db import models

# Create your models here.
class AirTicketModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, default=None)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    ticket_no = models.IntegerField()
    no_of_tickets = models.IntegerField()


