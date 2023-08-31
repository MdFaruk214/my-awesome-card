from django.shortcuts import render, HttpResponse

# Create Your viwes here.
from django.http import HttpResponse

def index(request):
   return render(request, 'shop/index.html')

def about(request):
   return HttpResponse("we are at about")

def contact(request):
   return HttpResponse ("we are at contact")

def tracker(request):
   return HttpResponse ("we are tracker")

def search(request):
   return HttpResponse("we are at search")

def prodview(request):
   return HttpResponse("we are at product view")

def checkout(request):
   return HttpResponse("we are at  checkout")

