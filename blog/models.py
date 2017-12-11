from django.db import models
from django.utils import timezone

class Post(models.Model):#this line defines the model, models.model means that it indicate django that it is our model and it needs to be saved in database
    author=models.ForeignKey('auth.user')#it is the link to another model
    title=models.CharField(max_length=200)#it is used when we want to limited no of characters
    text=models.TextField()#it is used for unlimited characters
    created_date=models.DateTimeField(default=timezone.now)#this is for date and time
    published_date=models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date=timezone.now()
    self.save()

def __str__(self):
    return self.title
    
