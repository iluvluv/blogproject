from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .models import Comment
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def main(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", {"blogs": blog})
#request는 블로그의 모든 글을 불러온다 , 블로그에서 불러온것을 blog템플릿에 넘겨준다
def input(request):
    return render(request, "new.html") 

def savedata(request):
    if request.method == "POST": 
        title = request.POST["title"]
        body = request.POST["body"]
        blog = Blog()
        blog.title = title
        blog.body = body
        blog.time = timezone.now()
        blog.save()
        return redirect('main')
    elif request.method == "GET":
        return render(request, "new.html") 

def update_page(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request,"update.html",{"blog": blog})

def update(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()
    return redirect('main')
    
def delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return redirect('main')

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    comment = Comment.objects.filter(blog=blog.id)
    return render(request, "detail.html", {"blog": blog, "comments": comment})

def comment_save(request,id):
    content = request.GET['content']
    comment = Comment()
    comment.content = content
    comment.time = timezone.now()
    comment.blog = get_object_or_404(Blog, pk=id)
    comment.save()
    blog = get_object_or_404(Blog, pk=id)
    return redirect('detail',id)

def comment_update_page(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request,"comment_update.html",{"comments": comment})

def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    content = request.GET['content']
    comment.content = content
    comment.save()
    return redirect('detail', comment.blog.id)

def comment_delete(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', comment.blog.id)

def sign_up(request):
    if request.method == "GET":
        return render(request,"sign_up.html")
    elif request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["pw"]   
        password_check = request.POST["pw_check"]
        #비밀번호 재확인 불일치
        if password != password_check:
            return render(request, "sign_up.html")
        #새로운 유저 생성
        user = User.objects.create_user(username=username, password=password)
        auth.login(request, user)
    return redirect("main")   
     
def sign_in(request):
    if request.method == "GET":
        return render(request,"sign_in.html")
    elif request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["pw"]   
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "sign_in.html")
    auth.login(request, user)
    return redirect("main")       

def sign_out(request):
    if request.method == "POST":
       if request.user.is_authenticated:
           auth.logout(request)
    return redirect("main")  



