
from django.contrib import admin
from django.urls import path
from Medicoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
]
