from django.shortcuts import render
from .models import Contacts
import uuid
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    data = Contacts.objects.all()
    return render(request, "index.html", {"data":data})

def new(request):
    return render(request , "new.html")

def add(request):
    name = request.POST['name']
    rel = request.POST['rel']
    num = request.POST['num']

    data = Contacts(unique_id=str(uuid.uuid4()),
        name=name,
        relationship=rel,
        mobile=num
    )
    data.save()
    return HttpResponseRedirect("/")

def views(request, id):
    data = Contacts.objects.get(unique_id=id)
    return render(request, "view.html", {"data" : data})

def e(request, id):
    data = Contacts.objects.get(unique_id=id)
    return render(request, "edit.html", {"data" : data})

def edit(request, id):
    data = Contacts.objects.get(unique_id=id)
    n = request.POST['name']
    r = request.POST['rel']
    num = request.POST['num']

    data.name = n
    data.relationship = r
    data.mobile = num
    data.save()

    return HttpResponseRedirect("/")