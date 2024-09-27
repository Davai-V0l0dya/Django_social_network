from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, UserProfile
from .forms import UserRegistrationForm, PostForm, CommentForm
from django.http import HttpResponseRedirect


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'social/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'social/register.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Устанавливаем автора поста
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'social/create_post.html', {'form': form})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profile_view(request, user_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'social/profile.html', {'profile': user_profile})