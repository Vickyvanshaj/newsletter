from django.db import models

class Mail(models.Model):
    mail=models.EmailField(max_length=100,blank=True,null=True,unique=True)