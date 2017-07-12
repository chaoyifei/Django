from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def team(request):
    return render(request,'team.html')
def member(requst):
    return render(requst,'member.html')
def research(request):
    return render(request,'research.html')
def lab_gallery(request):
    return render(request,'lab_gallery.html')
def contact(request):
    return render(request,'contact.html')
