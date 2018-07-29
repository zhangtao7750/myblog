from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def Homepage(request):
    posts=Post.objects.all()
    return render(request,'Homepage.html',{'posts':posts})