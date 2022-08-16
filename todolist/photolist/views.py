from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm

def photo_list(request):
    return render(request, 'photolist/photo_list.html')

def home(request):
    return render(request, 'photolist/home.html')

def account(request):
    return render(request, 'photolist/account.html')


def post_new(request):
    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    #         messages.success(request, '포스팅을 저장했습니다.')
    #         return redirect(post)
    #     else:
    #         form = PostForm()

    #     return render(request, 'photolist/post_form.html', {
    #         'form': form,
    #         'post': None
    #     })
    form = PostForm()
    return render(request, 'photolist/post_form.html', {
        'form': form
    })