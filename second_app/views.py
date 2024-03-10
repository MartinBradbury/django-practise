from django.shortcuts import render

# Create your views here.
def secondview(request):
    return render(request, 'second.html')