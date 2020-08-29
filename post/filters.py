 
''' POST FILETERS '''

import django_filters
from .models import Post
from user.models import User,Profile
from django.db.models import Q

import operator
from functools import reduce
'''
class PostFilter(django_filters.FilterSet):

	CHOICES=(
	('Latest','Latest'),
	('views', 'Views')
	)

	ordering = django_filters.ChocieFilter(label='sort',choices= CHOICES, method ='filter_by_order')

 
 	class Meta:
 		model = Post
 		fields = {
 				'titele' : ['icontains']
 		}


 	def filter_by_order(self,queryset,name,value):
 		return queryset.order_by('date_created')

'''


class PostFilter(django_filters.FilterSet):

	SORT_CHOICES=(
	('latest','Latest'),
	('views', 'Views'),
	('appreiations','Appreiations')
	)

	FILTER_CHOICES=(
	('all','All Posts'),
	('college', 'My College'),
	('following','Following')
	)

	title = django_filters.CharFilter(label='search', 
		method= 'filter_by_search')

	sorting = django_filters.ChoiceFilter(label='sort by',
		choices= SORT_CHOICES, method ='filter_by_sort', empty_label=None)

	filtering = django_filters.ChoiceFilter(label='filter by',
		choices= FILTER_CHOICES, method ='filter_by_filter', empty_label=None)


	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user')
		#print(self.user)
		super(PostFilter,self).__init__(*args,**kwargs)

	def filter_by_search(self,queryset,name,value):
		search_list=value.split()
		print(search_list)
		query = reduce(operator.and_ , (Q(title__icontains = item) for item in search_list))
		main_queryset =  queryset.filter(query)
		
		if main_queryset.count()<=10:
			for search_terms in search_list:
				second_queryset=queryset.filter(title__icontains=search_terms)
				main_queryset=main_queryset|second_queryset

		#second_queryset = queryset.filter(title__icontains='tags')
		return main_queryset 



	def filter_by_sort(self,queryset,name,value):
		if value=='latest':
			sort_by='-date_created'

		elif value=='views':

			sort_by = '-views'
		else:
			sort_by = '-likes'
		#print(self.user)
		return queryset.order_by(sort_by)

	

	def filter_by_filter(self,queryset,name,value):
		if value=='all':
			return queryset
		elif value=='college':
			college = self.user.user.college
			#print(self.user.user.username)
			return queryset.filter(Q(author__users__college__name=college)|
				Q(author__pages__college__name=college))
    
		else:
			sort_by = 'following'
			user_id = self.user.user.user.id 
			profile_instance = Profile.objects.get(users__id = user_id)
			follower_instances = profile_instance.followers.all()
			following_list=[]
			for i in follower_instances:
				following_list.append(i.to_profile)
			return queryset.filter(author__in = following_list)





	class Meta:
 		model = Post
 		fields = ('title',)

 		'''
 		fields = {
 				'title' : ['icontains']
 		}
		'''
 

class PostTagFilter(django_filters.FilterSet):

	SORT_CHOICES=(
	('latest','Latest'),
	('views', 'Views'),
	('appreiations','Appreiations')
	)

	sorting = django_filters.ChoiceFilter(label='sort by',
		choices= SORT_CHOICES, method ='filter_by_sort')

	#filtering = django_filters.ChoiceFilter(label='filter by',
	#	choices= FILTER_CHOICES, method ='filter_by_filter')



	def filter_by_sort(self,queryset,name,value):
		if value=='latest':
			sort_by='-date_created'

		elif value=='views':

			sort_by = '-views'
		else:
			sort_by = '-likes'
		print(sort_by)
		print(queryset.filter(sort_by))
		return queryset.filter(sort_by)

	class Meta:
 		model = Post

 		fields =('title',)
