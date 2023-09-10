from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from .forms import RecipePostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#url = reverse('login')

def homepages(request):
    posts = Post.objects.all()
    return render(request, "recipes/homepage.html", {'posts':posts})


#@login_required('main/login')
def uploadrecipe(request):
    if request.method == 'POST':
        form = RecipePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('recipes:homepages')  # redirect to user's list of posts
    else:
        form = RecipePostForm()
    return render(request, 'recipes/createPost.html', {'form': form})

#@login_required('main/login')
def personalrecs(request):
    curr_user = request.user
    posts = Post.objects.filter(author_id=curr_user.id)
    #print(curr_user.id)
    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'recipes/myrecipes.html', {'posts': posts})

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post.id)
    return render(request, "recipes/details.html", {"post":post})