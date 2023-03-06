from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Balu(request):
    return HttpResponse('<center><h1>He loves AKHILA</h1></center>')
def junaid(request):
    return HttpResponse('<marquee><h1>AKHIF loves DEEPTHI</h1></marquee>')