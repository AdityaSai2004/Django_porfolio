from django.shortcuts import render
from .models import Blogs
# Create your views here.
def all_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/index.html', {'blogs':blogs})