# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
   path('success/', views.success, name='success'),
    # other patterns
]
