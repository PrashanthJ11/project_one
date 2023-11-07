from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def Rishi(request):
    return HttpResponse("<h2><marquee>This is Rishi, i am from dharmavaram</marquee></h2>")