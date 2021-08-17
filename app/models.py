from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import models as tiny_models

# Create your models here

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/',default='SOME IMAGE')
    bio = tiny_models.HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    @receiver(post_save, sender=User)
    def save_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

class Languages(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_languages(self):
        self.save()


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField()
    description = tiny_models.HTMLField()
    url = models.URLField()
    images = models.ImageField(upload_to = 'images/',default='someimage',null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image_1 = models.ImageField(upload_to='projects/',default="project image")
    image_2 = models.ImageField(upload_to='projects/',default="project image")
    languages = models.ManyToManyField(Languages)

    def __str__(self):
        return self.title

    def save_project(slef):
        self.save()

