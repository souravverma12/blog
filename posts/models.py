from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):  #posts is our module
    title= models.CharField(max_length=100)
    body= models.CharField(max_length=1000000)
    created_at=models.DateTimeField(default=datetime.now,blank=True) #from datetime import datetime

