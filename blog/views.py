# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import BlogPost
# Create your views here.

def archive(request):
    posts=BlogPost.objects.all()
    return render_to_response('archive.html',{'posts':posts})

def about(request):
    return HttpResponse('blog say here is the about page')