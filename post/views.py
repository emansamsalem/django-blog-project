from django.shortcuts import render
#added
from .models import Post
from . forms import post_form
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def post_list(request):
    all_posts = Post.objects.all() #RETURNS all created objects
    return render(request,'post/post_list.html',{'all_posts':all_posts})



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


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'created_at']  # as it doesn't access forms.py file
    template_name = 'post/post_edit.html'  # as the need file is named post_edit and edit differs from update
    success_url = '/blog/cbv'   #redirected link when submit button is pressed

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'created_at','published', 'email','views_count', 'Category' ]  # as it doesn't access forms.py file
    template_name = 'post/post_create.html'
    success_url = '/blog/cbv'  # redirected link when submit button is pressed
