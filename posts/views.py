from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            #No, Show Error
            return HttpResponseRedirect(form.erros.as_jsonn())

    # get all posts, limit = 20
    posts = Post.objects.all().order_by("-created_at")[:20]

    # Show
    return render(request, 'posts.html',
                 {'posts': posts})

def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def LikeView(request,post_id):
    post=Post.objects.get(id=post_id)
    new_value=post.likes +1
    post.likes=new_value
    post.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post= Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=PostForm(PostForm)
        return render(request, 'edit.html',{'post':post, 'form': form})