from django.db import models

class usersInfo(models.Model):

    name = models.CharField(max_length=50 , blank=True , null= True )
    mailAddress = models.DateTimeField()




# Create your models here.
