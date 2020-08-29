


''' Project VIEWS '''

from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from user.models import *
# Create your views here.

def projects(request):
  return HttpResponse('<h1>Projects List</h1>')

def projectdetail(request,pk):
  p=Project.objects.get(slug=pk)
  return HttpResponse(f'<h1>Project List {p.title}</h1><p>Authored by {p.author}</p>')

def banner(request,pk):
  p=ProjectBanner.objects.get(slug=pk)
  return HttpResponse(f'<h1>Project Banner {p.heading}</h1><p>Authored by {p.owner}</p>')
  
def createproject(request,pk):
  p=Profile.objects.get(slug=pk)
  return HttpResponse(f'<h1>create project by {p}</h1>')
  
def updateproject(request,ppk,pk):
  p=Profile.objects.get(slug=pk)
  project=Project.objects.get(slug=ppk)
  return HttpResponse(
    f'<h1>Update project </h1><h6>by {p}</h6><p>{project.title}</p>')
   
def deleteproject(request,ppk,pk):
  p=Profile.objects.get(slug=pk)
  project=Project.objects.get(slug=ppk)
  return HttpResponse(
    f'<h1>Delete project </h1><h6>by {p}</h6><p>{project.title}</p>')