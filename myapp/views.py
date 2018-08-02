from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Post

# Create your views here.
def Homepage(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})
def Flight(request):
    posts=Post.objects.filter(title_item='flight')
    return render(request, 'flight.html', {"posts":posts})
def B737(request):
    posts=Post.objects.filter(title_item='b737')
    return render(request, 'b737.html', {"posts":posts})
def Python(request):
    posts=Post.objects.filter(title_item="python")
    return render(request, 'python.html', {"posts":posts})
def RedWine(request):
    posts = Post.objects.filter(title_item='redwine')
    return render(request,'redwine.html',{"posts":posts})






