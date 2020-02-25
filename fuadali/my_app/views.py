import request
from django.shortcuts import render
from bs4 import Beatifulsoup


# Create your views here.
def home(request):
    return render(request,'base.html')

def new_search(request):
    search = request.POST.get('search')
    stuff = {'search':search,}
    return render (request,'my_app/new_search.html',stuff  )

def tespage(request):
    return render (request,'my_app/tespage.html')
