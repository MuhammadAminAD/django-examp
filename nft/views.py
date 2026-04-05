from django.shortcuts import render

def home(request):
    return render(request, 'nft/home.html')

def explore(request):
    return render(request, 'nft/explore.html')

def detail(request):
    return render(request, 'nft/detail.html')

def become_artist(request):
    return render(request, 'nft/become_artist.html')

def faq(request):
    return render(request, 'nft/faq.html')
