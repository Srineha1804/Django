from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login1.html")

def RegistrationPage(request):
    return render(request,"register.html")
def About(request):
    return render(request,"about.html")
def Contactus(request):
    return render(request,"Contactus.html")
