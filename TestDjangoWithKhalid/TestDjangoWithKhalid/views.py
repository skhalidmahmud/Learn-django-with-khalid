from django.http import HttpResponse

def home(request):
    return HttpResponse("<b>Welcome to my new website.</b>\nIt is under constraction, so wait and see after 1 hr.\nBest of luck.")
