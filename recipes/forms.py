from django import forms
from .models import Post


class RecipePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
