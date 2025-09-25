from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Table
from django.template import loader

# Create your views here.

def index(request):
    return render(request,'main.html')

def all_members(request):
    mymembers = Table.objects.all().values()
    return render(request,'all_members.html',{"mymembers": mymembers})

def details(request, id):
    mymember = Table.objects.get(id=id)
    return render(request,'details.html',{"mymember": mymember})

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def delete_member(request,id):
    member = Table.objects.get (id=id)
    member.delete()
    return redirect("all_members")

def add(request):
    return render(request,'add.html')
def add_member(request):
    fname = request.POST["first_name"]
    lname = request.POST["last_name"]
    x=Table(firstname=fname,lastname=lname)
    x.save()
    return redirect('all_members')


def update(request):
    return render(request,'update.html')

def update_member(request, id):
    member = Table.objects.get (id=id)

    if request.method == "POST":
        member.firstname = request.POST.get("first_name")
        member.lastname = request.POST.get("last_name")
        member.save()
        return redirect("all_members")

    # if GET, show the form with prefilled values
    return render(request, "update.html", {"member": member})




# def add(request):
#     mymembers = Table.objects.all().values()
#     return render(request,'add.html',{"mymembers": mymembers})


# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))
