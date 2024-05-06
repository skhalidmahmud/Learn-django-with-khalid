from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':'Home page',
    }
    return render(request, "index.html", data)
def test(request):
    return HttpResponse("This is home on <b>Test<b> page.")
def testMore(request, urlss):
    return HttpResponse(urlss)