from django.shortcuts import render, redirect 
from .models import Post,Comment

def index(request):
    posts = Post.objects.all() 
    context= {
        "posts":posts
    } 
    return render(request,'index.html',context)
    
def read(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post":post
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

def c_create(request,post_id):
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user #request.user 는 현재 접속한 유저의 정보
        comment.post = Post.objects.get(id = post_id) # post_id 는 댓글을 단 post의 id(인증키)
        comment.content = request.POST['comment'] # comment는 text 창의 name
        anonymous = request.POST.get('anonymous',False)  
        if anonymous == "y":
            comment.anonymous = True
        comment.save()
        return redirect('index')


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
