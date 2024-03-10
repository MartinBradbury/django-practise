from django.shortcuts import render
from .models import Test, Article

# Create your views here.
def firstview(request):
    test = Test.objects.all()
    articles = Article.objects.all().order_by('date')
    
    
    return render(
        request,
        "index.html", 
        {
            'test': test,
            'articles': articles,
            
            
        },
    )

