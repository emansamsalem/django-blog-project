from django.shortcuts import render
#added
from .models import Post     #class name
# Create your views here.
def post_list(request):
   # print("hello eman")
    all_posts = Post.objects.all()
    return render(request, 'all_posts.html', {'all_posts':all_posts})



def post_detail(request,id):
    post = Post.objects.get(id = id)
    return render(request,'post.html',{'post':post})