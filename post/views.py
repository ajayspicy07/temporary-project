


''' Post VIEWS '''

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.utils import timezone
from datetime import timedelta
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django_filters.views import FilterView

from .models import *
from .forms import *
from .filters import *
from user.models import *

# Create your views here.

def posts(request):
  return HttpResponse('<h1>Posts List</h1>')



def postdetail(request,pk):
  


  def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')

    if address:
      ip = address.split(',')[-1].strip()
    else:
      ip=request.META.get('REMOTE_ADDR')
    return ip

  post=Post.objects.get(slug=pk)
  #print(request.session)
  key=post.slug
  session = request.session.get(key)
  if request.user.is_authenticated and get_ip(request) and not session:
    #if timezone.now()-request.user.user.previous_login>timedelta(minutes=1):
      #print('kljdsf;s')
      post.views+=1
      post.save()
      request.session[key]=True
  


  context={
  'post':post
  }
  #key=post.slug
  #print(request.user.last_login)
  #print(timezone.now())
  #diffrence = (timedelta(minutes=1))
  #print(diffrence)
  #print(timezone.now()-request.user.last_login>diffrence)
  #print(key)
  #print(request.session.get(key))

  #print(request.session._session_cache)



  return render(request,'post/postdetail.html',context)

 

class postdetailview(DetailView):
  model = Post
  template_name= 'post/postdetail.html'
  context_object_name='post'


def folder(request,pk):
  p=PostDirectory.objects.get(slug=pk)
  return HttpResponse(f'<h1>Folders {p.owner}</h1><p>Authored by {p.name}</p>')
  
class createpost(CreateView):
  model = Post
  form_class = PostCreationForm
  template_name = 'post/createpost.html'

  def form_valid(self, form):
      data = form.cleaned_data['tt']
      print(data)
      form.save()
      print(len(data))
  
      for i in data.split('--')[:-1]:
        try:
          #print(i,type(i))
          tag = Tag.objects.get(tag_name__iexact=i)
          #print(tag,tag.tag_name,tag.id)
          print('existing tag')
        except:
          tag = Tag.objects.create(tag_name=i)
          tag.save()
          print('non existing tag')
        form.instance.tags.add(tag)
      return super().form_valid(form)


def postlistview(request):
  context ={}
  college = request.user.user.college
  queryset=Post.objects.filter(Q(
        author__users__college__name = college)|Q(
      visibility='PUBLIC')|Q(author__pages__college__name=college))
      
  filterd_posts = PostFilter(
    request.GET,
       queryset = Post.objects.filter(Q(
        author__users__college__name = college)|Q(
      visibility='PUBLIC')|Q(author__pages__college__name=college)),
      user=request.user )
  #print(queryset)
  paginated_filterd_posts = Paginator(filterd_posts.qs,2)
  page_number = request.GET.get('page')
  posts_per_page = paginated_filterd_posts.get_page(page_number)


  context['posts_per_page'] = posts_per_page
  context['filterd_posts'] = filterd_posts
  #print(context['filterd_posts'].__dict__)
 
    
  return render(request,'post/postview.html',context=context)


class postlist(ListView):
  model = Post
  template_name = 'post/posts.html'
  #context_object_name = 'posts'
  paginate_by = 10
  ordering =[ '-date_created']
  
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    #print(self.request.user.user.college)
    #posts = Post.objects.all()
    college = self.request.user.user.college
    
    context['filter']= PostFilter(self.request.GET, 
      queryset=self.get_queryset().filter(Q(
        author__users__college__name = college)|Q(
        visibility='PUBLIC')|Q(author__pages__college__name=college)),
      user=self.request.user )

    paginated_filterd_posts = Paginator(context['filter'].qs,self.paginate_by)
    page_number = self.request.GET.get('page')
    posts_per_page = paginated_filterd_posts.get_page(page_number)
    context['posts_per_page'] = posts_per_page
  
    return context
  

def updatepost(request,pk):
  #p=Profile.objects.get(slug=pk)
  post=Post.objects.get(slug=pk)
  return HttpResponse(
    f'<h1>Update post </h1><h6>by  { post.author} </h6><p>{post.title}</p>')


class updatepostclass(UpdateView):
  model = Post
  form_class = PostUpdationForm
  template_name = 'post/createpost.html'

  def form_valid(self, form):
      data = form.cleaned_data['tt']
      print(data)
      form.save()
      print(len(data))
      print(form.instance.tags.clear())
  
      for i in data.split('--')[:-1]:
        try:
          #print(i,type(i))
          tag = Tag.objects.get(tag_name__iexact=i)
          #print(tag,tag.tag_name,tag.id)
          print('existing tag')
        except:
          tag = Tag.objects.create(tag_name=i)
          tag.save()
          print('non existing tag')
        form.instance.tags.add(tag)
      return super().form_valid(form)


  




   
def deletepost(request,ppk,pk):
  p=Profile.objects.get(slug=pk)
  post=Post.objects.get(slug=ppk)
  return HttpResponse(
    f'<h1>Delete post </h1><h6>by {p}</h6><p>{post.title}</p>')

''' This is  For Uservalidate in page members'''
def validatetag(request):
  value=request.GET.get('value',None)
  tag=Tag.objects.get(tag_name__iexact=value)
  print(tag)
  print(tag.id)
  return JsonResponse(tag,safe=False)

''' Tag auto complete in Post creation '''
def tagcomplete(request):
  if 'term' in request.GET:
    qs = Tag.objects.filter(tag_name__icontains=request.GET.get('term'))[:10]
    tags = []
    for tag in qs:
      tags.append(tag.tag_name)
      print(tag.tag_name)
    return JsonResponse(tags,safe=False)




def tagserach(request,pk):
  tag = Tag.objects.get(tag_name= pk)
  post= tag.post_set.all()
  context ={
  'post':post
  }
  print('Function Based view')
  return render(request,'post/tagsearch.html',context)

class posttagdetail(ListView):
  model = Post
  template_name = 'post/posts.html'
  #context_object_name = 'posts'
  #ordering =[ '-date_created']
  
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context['filter']= PostTagFilter(self.request.GET, 
      queryset=self.get_queryset().filter(tags=self.kwargs['pk']))
    print('class based view')
    return context
 


