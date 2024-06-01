from django.shortcuts import render
from datetime import datetime
from base.models import Contact
from django.contrib import messages

def home(request):
    return render(request , "home.html")
    # return HttpResponse("Hii")

def Our_story(request):
    return render(request , "our_story.html")

def Classics_Flavours(request):
    return render(request , "classics_flavours.html")

def Fruit_n_Nuts(request):
    return render(request , "fruit_n_nuts.html")

def Premium_Flavours(request):
    return render(request , "premium_flavours.html")

def Fancy_Flavours(request):
    return render(request , "fancy_flavours.html")

def Sofy(request):
    return render(request , "softy.html")

def Desserts(request):
    return render(request , "desserts.html")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Form has been submitted sucessfully!")
    return render(request , "contact.html")
      


