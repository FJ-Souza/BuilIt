from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import *
from myapp.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    card = AddMaterial.objects.all()
    return render(request, 'myapp/index.html', {'info': card})

def addMaterial(request):
    form = AddMateriaisForm
    if request.method == "POST":
        form = AddMateriaisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    return render(request,'myapp/addMaterial.html', {"form": form})


def edit(request, id):
    item = AddMaterial.objects.get(pk=id)
    form = AddMateriaisForm(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item = AddMaterial.objects.get(pk=id)
            form = AddMateriaisForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    item = AddMaterial.objects.get(pk=id)
    return render(request, "myapp/readMaterial.html", {"item":item})

def delete(request, id):
    item = AddMaterial.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

def listar(request):
    card = AddMaterial.objects.all()
    return render(request, 'myapp/listarMaterial.html', {'info': card})