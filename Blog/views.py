from __future__ import print_function
from django.conf import settings
from django.shortcuts import render, redirect
from Blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def Blogs(request):
    posts = Post.objects.all()[0:10]
    context = {'posts' : posts,
    'media_url': settings.MEDIA_URL
    }
    return render(request, 'Blog/Blogs.html', context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "Blog/BlogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST['parentSno']
        print(comment)
        if parentSno == "":
            comment_ob = BlogComment(comment=comment, user=user, post=post)
            comment_ob.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment_ob=BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment_ob.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f'/Blog/{post.slug}')

def upload(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        slug = request.POST['slug']
        content = request.POST['content']
        image = request.FILES['file']
        timeStamp = request.POST['timeStamp']

        blog_model = Post(title=title, author=author, content= content, slug=slug, image=image, timeStamp=timeStamp)
        blog_model.save()
        messages.success(request, "Your Blog has been posted successfully")

        # author = blog_model.author
        # Blogs = Post.objects.filter(name=str(request.user))

    return render(request, "Blog/upload.html")
