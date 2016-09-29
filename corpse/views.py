from django.shortcuts import render
from django.utils import timezone
from .models import Post
from  .forms import PostForm
from django.shortcuts import redirect

def post_list_end(request):
    last_post = Post.objects.latest('created_date')
    return render(request, 'corpse/post_list_end.html', {'last_post': last_post})
    
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'corpse/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'corpse/post_edit.html', {'form': form})