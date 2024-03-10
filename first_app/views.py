from django.shortcuts import render

# Create your views here.
def firstview(request):
    return render(request, "index.html")
