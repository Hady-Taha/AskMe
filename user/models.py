from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    userpro=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(upload_to='profileImage',default='profileImage/userAvatar.png')
    bio=models.CharField(max_length=50,null=True,blank=True)
    slug=models.SlugField(blank=True, null=True)
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(str(self.userpro))
        super(Profile,self).save(*args,**kwargs)
            
    
    
    def __str__(self):
        return str(self.userpro)


def createprfile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(userpro=kwargs['instance'])
    pass
    
post_save.connect(createprfile,sender=User)