from django.db import models
from chat.models import UserProfile

# Create your models here.
class ChatReg(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()