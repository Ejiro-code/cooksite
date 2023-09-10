from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('home', views.homepages, name='homepages'),
    path('uploadrecipe', views.uploadrecipe, name='uploadrecipe'),
    path('personalrecs', views.personalrecs, name='personalrecs'),
    path('<int:pk>/details/', views.details, name='details'),
]
