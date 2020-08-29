


''' POST URLS '''

from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
  
    path('posts/',  views.postlist.as_view() , name="Posts"),
    path('postslist/', views.postlistview, name="postslist"),
    path('posts/<slug:pk>/', views.postdetail, name="Post_Details"),
    path('folders/<slug:pk>/', views.folder, name="Folder"),
    
    path('createpost/', views.createpost.as_view(), name="Create_Post"),
    path('postdetail/<slug:slug>/', views.postdetailview.as_view(), name= "postdetail"),
    path('updatepost/<slug:slug>/', views.updatepostclass.as_view(), name= "updatepost"),
    #path('<slug:ppk>/<slug:pk>/updatepost/', views.updatepost, name="Update_Post"),
    path('<slug:pk>/updatepost/', views.updatepost, name="Update_Post"),
    
    path('<slug:ppk>/<slug:pk>/deletepost/', views.deletepost, name="Delete_Post"),
    
    path('validate-tag/' , views.validatetag, name='validate-tag'),
    path('tag_complete', views.tagcomplete , name='tag_complete'),

    path('tagserach/<pk>/', views.tagserach, name= 'searchtag'),
    path('tagserachs/<pk>/' , views.posttagdetail.as_view(), name='tagserachs'),
]


