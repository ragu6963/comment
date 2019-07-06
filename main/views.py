from django.shortcuts import render, redirect 
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-updated_at')
    context= {
        "posts":posts
    } 
    return render(request,'index.html',context)
    
def read(request,post_id):
    post = Post.objects.get(id=post_id) # get은 조건에 맞는 1개
    context = {
        "post":post,
    }
    return render(request,'read.html',context)

def create(request): 
    if request.method == "GET":
        return render(request,'create.html') 

    elif request.method == "POST":
        post = Post() 
        post.user = request.user 
        post.title = request.POST['title']
        post.content = request.POST['content']  
        post.save() 
        return redirect(index)  

def update(request,post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context={
            "post":post
        }
        return render(request,'update.html',context)
    
    elif request.method == "POST":  
        post = Post.objects.get(id=post_id)
        post.title = request.POST['title']
        post.content = request.POST['content'] 
        post.save() 
        return redirect(index) 

def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect(index)
