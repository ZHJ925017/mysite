# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import BlogPost,Category,Page
# Create your views here.

def archive(request):
    posts=BlogPost.objects.all()
    return render_to_response('archive.html',{'posts':posts})

def about(request):
    #return HttpResponse('blog say here is the about page')
    return render(request,'blog/about.html')

def index(request):
    #construct a dictionary to  pass to the template engine as its context.
    #Note the key boldmessage is the same as {{boldmessage}} in the template!
    #context_dict={'boldmessage':"crunchy,creamy,cookie,candy,cupcake!"}.

    category_list=Category.objects.order_by('-likes')[:5]
    context_dict={'categories':category_list}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier.
    #Note that the first parameter is the template we wish to use.
    return render(request,'blog/index.html',context_dict)

def show_category(request,category_name_slug):
    context_dict={}
    try:
        category=Category.objects.get(slug=category_name_slug)
        pages=Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Category.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request,'blog/category.html',context_dict)