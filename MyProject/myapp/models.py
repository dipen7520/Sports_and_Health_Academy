from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=14)
    textmsg = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name

# class Booking(models.Model):
# class History(models.Model):
# class (models.Model):
# class History(models.Model):