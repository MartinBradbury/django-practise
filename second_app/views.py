from django.shortcuts import render
from first_app.models import Test, Article, Space

# Create your views here.
def secondview(request):
    space = Space.objects.all().order_by('flagged')
    return render(
        request,
        "second.html", 
        {
            'space': space,  
        },
    )

   
  