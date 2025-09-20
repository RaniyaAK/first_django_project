from django.http import HttpResponse
from django.shortcuts import render
from .models import Table

# Create your views here.

def index(request):
    return render(request,'main.html')

def all_members(request):
    mymembers = Table.objects.all().values()
    return render(request,'all_members.html',{"mymembers": mymembers})

def details(request, id):
    mymember = Table.objects.get(id=id)
    return render(request,'details.html',{"mymember": mymember})

