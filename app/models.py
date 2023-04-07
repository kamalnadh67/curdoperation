from django.db import models


# Create your models here.
class TOPIC(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True) 

    def __str__(self):
        return self.topic_name
    

class Webpages(models.Model):
    topic_name=models.ForeignKey(TOPIC,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)
    url=models.URLField()
    def __str__(self):
        return self.topic_name
    




