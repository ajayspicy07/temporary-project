from django import template

register = template.Library()

@register.simple_tag
def my_paginate_example(value,field_name,urlencode=None):
	print('value :',value)
	print('field_name :', field_name)

	url = '?{}={}'.format(field_name,value)
	print('start url :',url)
	if urlencode:
		print('urlencode :', urlencode)
		querystring = urlencode.split('&')
		print('querystring :',querystring)
		filtered_querystring = filter(lambda p:p.split('=')[0]!=field_name,querystring)
		print('fq  :',filtered_querystring)
		encoded_querystring = '&'.join(filtered_querystring)
		url = '{}&{}'.format(url,encoded_querystring)
	print('final url :',url)

	return url
@register.simple_tag
def my_paginate_url(value,field_name,urlencode=None):
	#print('value :',value)
	#print('field_name :', field_name)

	url = '?{}={}'.format(field_name,value)
	#print('start url :',url)
	if urlencode and urlencode[:4]!='page':
		url = '{}={}'.format(field_name,value)
		#print('urlencode :', urlencode)
		querystring = urlencode.split('&')
		#print('querystring :',querystring)
		filtered_querystring = filter(lambda p:p.split('=')[0]!=field_name,querystring)
	
		encoded_querystring = '&'.join(filtered_querystring)
		url = '?{}&{}'.format(encoded_querystring,url)
	#print('final url :',url)

	return url
