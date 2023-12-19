from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    
    path('doctor/',views.doctor,name='doctor'),
    path('appointment/',views.appointment,name='appointment'),
    path('cardiologist/',views.cardiologist,name='cardiologist'),
    path('ecg/',views.ecg,name='ecg'),
    path('seniorheartsurger/',views.seniorheartsurger,name='seniorheartsurger'),
    path('gallery/',views.gallery,name='gallery'),
    path('home/',views.home,name='home'),
    path('success/',views.succes,name='success'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)