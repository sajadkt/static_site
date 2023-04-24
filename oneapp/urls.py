from django.conf.urls.static import static
from newone import settings
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.demo,name='demo'),
    path('newapp1/', include('newapp1.urls')),
  #  path('about/',views.about,name='about'),
  #  path('contact/',views.contact,name='contact')
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)