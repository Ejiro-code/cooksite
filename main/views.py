from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm  # , PostForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from .models import Post
from recipes.views import homepages

# Create your views here.


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            url = reverse("recipes:homepages")
            return redirect(url)
        else:
            messages.error(
                request, 'Invalid login Credentials. Please try again')
    return render(request, 'registration/login.html')


# @login_required(login_url="/login")
# def home(request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         post_id = request.POST.get("post-id")
#         # get the post
#         post = Post.objects.filter(id=post_id).first()
#         if post and post.author == request.user:
#             post.delete()

#     return render(request, 'main/home.html', {"posts": posts})


# @login_required(login_url="/login")
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             # Commit is set to false because we don't want it added to the database until the username is included
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect("/home")
#     else:
#         form = PostForm()

#     return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            url = reverse('recipes:homepages')
            return redirect(url)
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
