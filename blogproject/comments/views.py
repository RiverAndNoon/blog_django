from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
# Create your views here.
from .models import Comment
from .forms import CommentForm


def post_comment(request,post_pk):
    print("uiyuiy")
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            #redirect()函数可以
            #会根据get_absolut_url方法返回的url值进行重定向
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,'form':form,'comment_list':comment_list}
            return render(request,'blog/detail.html',context=context)
    else:
        return redirect(post)

