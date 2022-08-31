from django.shortcuts import render

# def home(request):
#     return render(request,'index.html')

# Create your views here.
from.models import Post

def home(request):
    post=Post.objects.all()
    context={'post':post}
    return render(request,'index.html',context)
