


''' POST ADMIN '''

from django.contrib import admin
from .models import *
# Register your models here.

class PostProjectAdmin(admin.ModelAdmin):
  
  list_display=('title', 'slug' , 'author', 'likes','views', 'get_college_name', 'visibility' ,'date_created' , 'last_modified', )
  
  list_filter=('author', 'visibility')
  search_fields=('title',)
  ordering =('likes','views')
  
  def get_college_name(self, obj):
        
        return obj.author.college()
  get_college_name.short_description = 'College'

  


  class Meta:
    abstract = True


class PostDirectoryAdmin(admin.ModelAdmin):
  list_display=('name','owner','total','date_created')
  list_filter=('date_created',)
  search_fields=('name',)
  
  def total(self, obj):
     return obj.directory.count()
     
  total.short_description = 'Total Posts'
 
  
  
class  PostAdmin(PostProjectAdmin):
  
    pass
  
  
  
  

admin.site.register(Tag)

admin.site.register(Post,PostAdmin)

admin.site.register(PostDirectory,PostDirectoryAdmin)