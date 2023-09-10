from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        # Creating a new user
        model = User
        # assigning these fields to a certain user
        fields = ["username", "email", "password1", "password2"]


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "description"]
