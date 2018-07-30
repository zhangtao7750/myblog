from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def Homepage(request):
    posts=Post.objects.all()
    return render(request,'Homepage.html',{'posts':posts})
def Index_Flight(request):
    posts=Post.objects.filter(title_item='flight')
    return render(request,'index_flightbasic.html',{"posts":posts})
def Index_B737(request):
    posts=Post.objects.filter(title_item='b737')
    return render(request,'index_B737.html',{"posts":posts})
def Index_Python(request):
    posts=Post.objects.filter(title_item='python')
    return render(request,'index_python.html',{"posts":posts})
def Index_RedWine(request):
    posts=Post.objects.all()
    return render(request,'index_redwine.html',{"posts":posts})