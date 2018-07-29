from django.shortcuts import render
from django.http import HttpResponse
from .models import PostB737,PostFlight

# Create your views here.
def Homepage(request):
    posts_flight=PostFlight.objects.all()
    return render(request,'Homepage.html',{'posts':posts_flight})
def Index_FlightBasic(request):
    posts_b737=PostB737.objects.all()
    return render(request,'index_flightbasic.html',{'posts_flight':posts_b737})