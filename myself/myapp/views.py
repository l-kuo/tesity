from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    # return HttpResponse("this is home page")
    return render(request, "myapp/index.html",{"title":"Home"})
def about (request):
    return render(request,"myapp/about.html",{"title":"About"})