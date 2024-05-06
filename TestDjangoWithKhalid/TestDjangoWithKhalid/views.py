from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':'Home page',
        'prople_details':[
            {'name':'Khalid Mahmud','phone':8801403001026},
            {'name':'Sabbir Hassan','phone':8801791501045}
        ]
    }
    return render(request, "index.html", data)
def test(request):
    return HttpResponse("This is home on <b>Test<b> page.")
def testMore(request, urlss):
    return HttpResponse(urlss)