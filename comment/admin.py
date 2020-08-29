from django.contrib import admin

# Register your models here.




''' COMMENT ADMIN '''

from django.contrib import admin
from .models import *

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
  list_display=('content_object', 'question' ,
  'get_type','date_created','count')
  list_filter=('date_created',)
  
  def get_type(self,obj):
      return obj.content_type.name
      
  def count(self,obj):
      return obj.reply_set.count()
    
  get_type.short_description = 'Type'
  count.short_description = 'Total Replies'
  
  
class ReplyAdmin(admin.ModelAdmin):
  list_display=('for_comment','answer','date_created')
  list_filter=('date_created', 'for_comment')
  


admin.site.register(Comment, CommentAdmin)

admin.site.register(Reply,ReplyAdmin)