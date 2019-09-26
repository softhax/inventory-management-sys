from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptop',
    }
    return render(request, 'index.html', context)


def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktop',
    }
    return render(request, 'index.html', context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobile',
    }
    return render(request, 'index.html', context)


def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)


def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = cls(instance=item)
            return render(request, 'edit_item.html', {'form': form})


def edit_laptop(request,pk):
    return edit_device(request, pk, Laptop, LaptopForm)


def edit_desktop(request,pk):
    return edit_device(request, pk, Desktop, DesktopForm)


def edit_mobile(request,pk):
    return edit_device(request, pk, Mobile, MobileForm)

def delete_device(request, pk, model):
    model.objects.filter(id=pk).delete()
    items=model.objects.all()
    context={
        'items':items
    }
    return render(request,'index.html',context)


def delete_laptop(request,pk):
    return delete_device(request, pk, Laptop)


def delete_desktop(request,pk):
    return delete_device(request, pk, Desktop)


def delete_mobile(request,pk):
    return delete_device(request, pk, Mobile)

# def add_laptop(request):
#     if request.method == "POST":
#         form=LaptopForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = LaptopForm()
#         return render(request, 'add_new.html', {'form': form})
#
# def add_desktop(request):
#     if request.method == "POST":
#         form=DesktopForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = DesktopForm()
#         return render(request, 'add_new.html', {'form': form})
#
#
# def add_mobile(request):
#     if request.method == "POST":
#         form=MobileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = MobileForm()
#         return render(request, 'add_new.html', {'form': form})
