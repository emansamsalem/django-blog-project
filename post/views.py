from django.shortcuts import render
#added
from .models import Post
from . forms import post_form

def post_list(request):
    all_posts = Post.objects.all() #RETURNS all created objects
    return render(request,'post/all_posts.html',{'all_posts':all_posts})



def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request,'post/post_detail.html',{'post':post})



def post_create(request):
    if request.method =="POST":
        form = post_form(request.POST) #to take send data to data base
        if form.is_valid():
            form.save()
    else:
        form = post_form() # to return empty form to fill it
    return render(request, 'post/post_create.html',{'form':form})




def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = post_form(request.POST,instance=post)
        if form.is_valid():
            form.save()
    else:
        form = post_form(instance=post)
    return render(request, 'post/post_edit.html', {'form': form})

