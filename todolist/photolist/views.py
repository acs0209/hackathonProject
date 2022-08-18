from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post
from django.views.generic import DetailView

# def photo_list(request):
#     return render(request, 'photolist/photo_list.html')

def photo_list(request): 
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    messages.info(request, 'messages 테스트')
    # instagram/templates/instagram/post_list.html
    return render(request, 'photolist/photo_list.html', {
        'photo_list': qs,
        'q': q ,
    })

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

photo_detail = PostDetailView.as_view()

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