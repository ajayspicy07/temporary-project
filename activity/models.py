

''' ACTIVITY MODEL '''

from django.db import models
from post.models import Post 
from project.models import Project
from user.models import Profile

from django.utils import timezone


from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.

''' BASE ACTIVITY  MODEL '''
class Activity(models.Model):
  limit = models.Q(model='post') | models.Q(model ='project')

  content_type = models.ForeignKey(
        ContentType,
       on_delete=models.CASCADE,
        limit_choices_to=limit,
        
        blank=False,
        null=False
    )

  object_id = models.PositiveIntegerField(
        
        null =False,
        blank=False,
    )

  content_object = GenericForeignKey('content_type', 'object_id')
    
  user=models.ForeignKey(Profile,on_delete=models.CASCADE)
  
  class Meta:
    abstract =True
  
''' Like Model '''
 
class Like(Activity):
  
    
    liked = models.BooleanField(default=False)
   
    
    def __str__(self):
       return str(self.content_object)
       
       
''' Save Model '''
class Saved(Activity):
  
  
  date_created = models.DateTimeField(default=timezone.now) 
  
  def __str__(self):
    return str(self.user)
  
  
   
  
  
 