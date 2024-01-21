from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_link = models.URLField(max_length=200)
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)
    event_image = models.ImageField(upload_to='images/')
    event_descp = models.TextField()
    event_location = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.event_name


class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user_name = models.CharField(max_length=200)
    user_pic = models.ImageField(upload_to='images/user/')
    user_no = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
