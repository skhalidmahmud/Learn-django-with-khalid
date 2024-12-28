from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
def test(request):
    return HttpResponse("This is home on <b>Test<b> page.")
def testMore(request, urlss):
    return HttpResponse(urlss)

def calculator(request):
    return render(request, "calculator.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def hire(request):
    return render(request, "hire-us.html")