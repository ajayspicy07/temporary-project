



''' POST MODELS '''

from django.db import models
from django.utils import timezone
from django.utils.text import slugify as inbuilt_slugify
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.urls import reverse
from slugify import UniqueSlugify,Slugify
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from user.models import *
#from comment.models import Comment


''' some logic '''
custom_slugify = Slugify()

# Create your models here.




''' Tags List '''
class Tag(models.Model):
  tag_name=models.CharField(max_length=100)
  
  
  def __str__(self):
    return self.tag_name


''' Base Post Model '''
class BasePost(models.Model):
  VISIBILITY = [
    ('PUBLIC', 'Public' ),
    ('PRIVATE', 'My College Only' ),
    ]
  COMMENTS = [
    ('ENABLE', 'Enable' ),
    ('Disable', 'Disable' ),
    ]
  COLLEGE_VISIBILITY = [
    ('YES', 'Yes' ),
    ('NO', 'No' ),
    ]
  
  
  author      =models.ForeignKey(Profile,on_delete =models.CASCADE)
  title       =models.CharField(max_length=400)
  slug        =models.SlugField(max_length=400,unique=True,blank=True)
  description =models.TextField()
  #body        = RichTextUploadingField()
  body       = HTMLField()
  tags        =models.ManyToManyField(Tag , blank=True)
  likes       =models.PositiveIntegerField(default=0)
  views       =models.PositiveIntegerField(default=0)
  
  comments    =models.CharField(max_length=10, choices=COMMENTS ,default='ENABLE')
  
  visibility  =models.CharField(max_length=10, choices=VISIBILITY ,default='PRIVATE')
  
  college_visibility   = models.CharField(max_length=10,choices=COLLEGE_VISIBILITY ,default='YES')
  
  date_created = models.DateTimeField(default=timezone.now) 
  last_modified = models.DateTimeField( auto_now=True)
  
  class Meta:
    abstract = True
  
  def __str__(self):
    return self.title
    
  def save(self, *args, **kwargs):
    self.slug=custom_slugify(self.title, allow_unicode=True)
    print(self.body)
    super().save(*args, **kwargs)
    
    
    
''' Base Folder '''
class BaseFolder(models.Model):
  owner = models.ForeignKey(Profile,
       on_delete=models.CASCADE)
  name = models.CharField(max_length=400)
  slug = models.SlugField(max_length=400,unique=True,blank=True)
  date_created = models.DateTimeField(default=timezone.now) 
  
  class Meta:
    abstract = True
  
  def __str__(self):
    return self.name
    
  def save(self, *args, **kwargs):
    self.slug=inbuilt_slugify(self.name, allow_unicode=True)
    super().save(*args, **kwargs)
  
    
    
    
    
''' Post Model '''
class Post(BasePost):
  #comment_model = GenericRelation('comment.Comment', related_query_name='posts')
  #liked= GenericRelation('activity.Like', related_query_name='postlikes')
  #saved= GenericRelation('activity.Saved', related_query_name='postsaved')
  

  def get_absolute_url(self):

    return reverse('post:postdetail', kwargs={'slug':self.slug})
  
  
''' Post directory '''
class PostDirectory(BaseFolder):
 
  directory = models.ManyToManyField(Post,blank=True,)
  
    
    
    
    