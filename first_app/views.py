from django.shortcuts import render
from .models import Test, Article, Space

# Create your views here.
def firstview(request):
    tests = Test.objects.all()
    articles = Article.objects.all().order_by('date')
    space = Space.objects.all().order_by('flagged')
    
    
    return render(
        request,
        "index.html", 
        {
            'tests': tests,
            'articles': articles,
            'space': space,
            
            
        },
    )

