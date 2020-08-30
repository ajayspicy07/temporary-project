



''' USER MODEL '''

from django.db import models
from django.utils.text import slugify as inbuilt_slugify

from django.contrib.auth.models import User as auth_user
from django.utils import timezone
from slugify import UniqueSlugify,Slugify
from PIL import Image

from django.urls import reverse
#from django.shortcuts import redirect

from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

''' some logic '''
#custom_slugify = UniqueSlugify()

custom_slugify=Slugify()



# Create your models here.

''' College list '''
class College(models.Model):
  name    =models.CharField(max_length=200)
  district=models.CharField(max_length=100)
  state   =models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

''' User MOdel '''
class User(auth_user):
  
  TYPE =[
    ('STUDENT','student'),
    ('EDUCATOR','Proffesor/Teacher/Educator')
    ]
  
  college     = models.ForeignKey(College,on_delete=models.SET_NULL,null=True)
    
  dob         = models.DateField(blank=False)
  user_mode   = models.CharField(max_length=10, choices=TYPE, default ='STUDENT')
  date_created  = models.DateTimeField(auto_now_add=True, blank=False)
  #previous_login = models.DateTimeField(default=timezone.now)
  profile      = GenericRelation('Profile', related_query_name='users')


  
  
      
  def full_name(self):
    return self.first_name+' ' +self.last_name
  
  def profile_name(self):
    return self.username
  
  def is_page(self):
    
    return False
  
  def __str__(self):
    return self.first_name+' ' +self.last_name


  


class Page(models.Model):
  name        =models.CharField(max_length=600)
  members     =models.ManyToManyField( User)
  college     =models.ForeignKey(College,on_delete=models.CASCADE, blank= True, default=1)
  date_created=models.DateTimeField(auto_now_add=True, blank=False) 
  profile      = GenericRelation('Profile', related_query_name='pages') 

  
  def full_name(self):

      return self.name

    
  def profile_name(self):
    return self.name
  
  def is_page(self):
    return True
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('user:home' ,kwargs={})
 


class Profile(models.Model):
 

    limit = models.Q(model='user') | models.Q(model ='page')

    content_type = models.ForeignKey(
        ContentType,
       on_delete=models.CASCADE,
        limit_choices_to=limit,
        
        blank=False,
    )

    object_id = models.PositiveIntegerField(
        blank=True,
        null =False
    )

    content_object = GenericForeignKey('content_type', 'object_id')
    
    slug =models.SlugField(blank=True,unique=True)
    img = models.ImageField( default='profile_pics/default.png',upload_to='profile_pics')
    description = models.TextField(default='hai',blank=True)


    @property
    def college(self):
      return str(self.content_object.college)
 
    
    def __str__(self):
        return self.content_object.full_name()
       
    def save(self, *args, **kwargs):

       self.slug=custom_slugify(self.content_object.profile_name(), allow_unicode=True)
       super().save(*args, **kwargs)
       
       img = Image.open(self.img.path)
       if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.img.path)
    
    def college(self):
    
      return str(self.content_object.college)
 



class Follower(models.Model):
  from_profile =models.ForeignKey(Profile,on_delete=models.CASCADE,
   related_name='followers')
  
  to_profile   =models.ForeignKey(Profile,on_delete=models.CASCADE, 
    related_name='following')
  
  date_created =models.DateTimeField(auto_now_add=True) 
  
  def __str__(self):
    return str(self.from_profile) +' follow '+ str(self.to_profile)
    
  
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



