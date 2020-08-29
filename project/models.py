

''' PROJECT MODELS '''


from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from user.models import *


#from comment.models import Comment
from post.models import BasePost, Tag

# Create your models here.


''' project model '''
class Project(BasePost):
 #comment_model = GenericRelation('comment.Comment', related_query_name='projects')
 #liked= GenericRelation('activity.Like', related_query_name='projectlikes')
 #saved= GenericRelation('activity.Saved', related_query_name='projectsaved')
  pass
  
  
''' Project Banner '''
class ProjectBanner(models.Model):
  owner = models.ForeignKey(Profile,
       on_delete=models.CASCADE)
  heading = models.CharField(max_length=600)
  slug = models.SlugField(max_length=600,unique=True,blank=True)
  skills_required= models.CharField(max_length=600)
  body=  models.TextField()
  date_created = models.DateTimeField(default=timezone.now) 
  #comment_model = GenericRelation('comment.Comment', related_query_name='projectsbanner')
  
  def __str__(self):
    return self.heading
    
  def save(self, *args, **kwargs):
    self.slug=slugify(self.heading, allow_unicode=True)
    super().save(*args, **kwargs)
    