from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jinja_tags(request):
    d={'name':'my name is kiran',
    'age':23}
    return render(request,'jinja_tags.html',context=d)