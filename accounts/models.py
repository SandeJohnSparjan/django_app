from django.db import models
from django.contrib.auth.models import User
#signals allow certain senders to notify a set of receivers that some action has taken place
from django.db.models.signals import post_save

#creating custom objects
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager,self).get_queryset().filter(city='Denton')

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city= models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',blank=True)
    #to display names in UserProfile Module
    def __str__(self):
        return self.user.username

    #creating an object named denton
    #in shell use this cmd UserProfile.denton.all()
    denton = UserProfileManager()

#receiver function to which signal is sent
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile= UserProfile.objects.create(user = kwargs['instance'])




#to receive a signal, registering receiver(create_profile) function using connect() method
#fn() called when signal is sent
post_save.connect(create_profile, sender = User)