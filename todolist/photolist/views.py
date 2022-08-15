from django.shortcuts import render

def photo_list(request):
    return render(request, 'photolist/photo_list.html')

def home(request):
    return render(request, 'photolist/home.html')

def account(request):
    return render(request, 'photolist/account.html')
