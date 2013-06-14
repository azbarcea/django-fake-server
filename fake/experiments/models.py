from django.db import models
from django.utils import timezone

# Create your models here.

class Test(models.Model):
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    prod_left = models.CharField(max_length=200)
    prod_right = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add = True)
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField()
    weight_left = models.IntegerField()
    weight_right = models.IntegerField()    
    history = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description

    def duration(self):
        return 0 if self.start_date is None else timezone.now() - self.start_date

