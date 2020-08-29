
''' POST FORMS'''

from .models import Post,Tag
from django import forms
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


''' USER FORMS '''


from .models import *



class PostCreationForm(forms.ModelForm):
  tt = forms.CharField(widget=forms.TextInput())
  #body = forms.CharField(widget=CKEditorWidget())
   
  #body = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 30}))

  #body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
  

  class Meta:
    model = Post
    fields = (
    	'author',
    	'title',
    	'description',
    	'body',
        'tt',
    	'comments',
    	'visibility',
    	'college_visibility'
    	)


class PostUpdationForm(forms.ModelForm):
  
  def hai(self):
    print(self.man)
    return self.man


  tt = forms.CharField(widget=forms.TextInput())
  #body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
  

  class Meta:
    model = Post
    fields = (
        'title',
        'description',
        'body',
        'tt',
        'comments',
        'visibility',
        'college_visibility'
        )


  def __init__(self,*args,**kwargs):
    #self.man = kwargs.pop('man')
    #self.man = 'Hai'
    
    super(PostUpdationForm,self).__init__(*args,**kwargs)
    tagstring=''
    for tags in self.instance.tags.all():
        tagstring+=tags.tag_name+'--'

    self.fields['tt'].widget.attrs['value']=tagstring
    #print('hello :',self.instance.tags.all())

  '''

  form.  


  '''







