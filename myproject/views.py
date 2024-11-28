from django.shortcuts import render
from .models import MyProject
from .models import GuestBook
from django.shortcuts import redirect

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def my_project(request):
    projects = MyProject.objects.all()
    return render(request, 'my_project.html', {'projects': projects})

def guest_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        message = request.POST['message']
        GuestBook.objects.create(name=name, address=address, message=message)
        return redirect('guest_book')
    
    guests = GuestBook.objects.all()
    return render(request, 'guest_book.html', {'guests': guests})