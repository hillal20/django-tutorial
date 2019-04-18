
from django.urls import path, re_path
from . import views 
app_name = 'article'
urlpatterns = [
   
 
    path('',views.articles, name ='list'),
    re_path('^(?P<slug>[\w-]+)/$',views.articledetail, name ='detail')
]