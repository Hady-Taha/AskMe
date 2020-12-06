from django.db import models
from user.models import Profile
from django.utils.text import slugify
# Create your models here.
class Message(models.Model):
    messages=models.TextField() 
    userProfile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    slug=models.SlugField(blank=True, null=True)
    def __str__(self):
        return str(self.userProfile)


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(str(self.userProfile))
        super(Message,self).save(*args,**kwargs)

