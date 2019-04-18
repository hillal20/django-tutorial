
from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static  import static 
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('account/', include('accounts.urls')),
    path('login/', include('accounts.urls')),
    path('home/',views.home),
    path('article/', include('articleApp.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)