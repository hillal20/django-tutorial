from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def articles(request):
   print('====> hilal')
   a = Article.objects.all().order_by('date')

   return render(request,'article/article.html', {'articles':a})

def articledetail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.filter(slug=slug)
    print(dir(Article.objects))
    
    print('======>',article[0])
    return render(request, 'article/articleDetail.html', {'article':article[0]})