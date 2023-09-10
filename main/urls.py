from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.custom_login, name='login'),
    # path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    # path('create-post', views.create_post, name='create_post'),
]
