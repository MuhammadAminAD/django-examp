from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import NFT, Feature, FAQ, Team, Partner, Category
from django.db.models import Q
import json
from django.contrib import messages

def home(request):
    nfts = NFT.objects.all().order_by('-created_at')[:4]
    features = Feature.objects.all()
    teams = Team.objects.all()
    partners = Partner.objects.all()
    context = {
        'nfts': nfts,
        'features': features,
        'teams': teams,
        'partners': partners,
    }
    return render(request, 'nft/home.html', context)

def explore(request):
    nfts = NFT.objects.all()
    
    q = request.GET.get('q', '')
    if q:
        nfts = nfts.filter(Q(title__icontains=q) | Q(details__description__icontains=q))
        
    category_filter = request.GET.get('category', '')
    if category_filter:
        nfts = nfts.filter(category__name=category_filter)
        
    sort = request.GET.get('sort', '')
    if sort == 'price':
        nfts = nfts.order_by('price')
    elif sort == '-price':
        nfts = nfts.order_by('-price')
    elif sort == '-created_at':
        nfts = nfts.order_by('-created_at')
    else:
        nfts = nfts.order_by('-created_at')
        
    context = {
        'nfts': nfts,
        'q': q,
        'selected_category': category_filter,
        'sort': sort,
    }
    return render(request, 'nft/explore.html', context)

def detail(request, pk=None):
    if pk:
        nft = get_object_or_404(NFT, pk=pk)
    else:
        nft = NFT.objects.first()
    context = {
        'nft': nft,
    }
    return render(request, 'nft/detail.html', context)

def become_artist(request):
    return render(request, 'nft/become_artist.html')

def faq(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'General')
    
    faqs = FAQ.objects.filter(category=category)
    if query:
        faqs = faqs.filter(question__icontains=query)
        
    context = {
        'faqs': faqs,
        'query': query,
        'selected_category': category,
    }
    return render(request, 'nft/faq.html', context)

def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False})

def register_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Username already exists'})
                
            user = User.objects.create_user(username=username, email=email, password=password)
            auth_login(request, user)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False})

def logout_view(request):
    auth_logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'nft:home'))

@login_required(login_url='/')
def purchase_nft(request, pk):
    nft = get_object_or_404(NFT, pk=pk)
    
    # Simulate purchase logic here
    # Send email notification
    subject = f"Receipt: Purchase of {nft.title}"
    body = f"Hello {request.user.username},\n\nYou have successfully purchased {nft.title} for {nft.price} ETH.\n\nThank you for using NFT Distro!"
    
    user_email = request.user.email if request.user.email else f"{request.user.username}@example.com"
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
    
    messages.success(request, f"Successfully purchased {nft.title}! Check your email for receipt.")
    return redirect('nft:detail_pk', pk=nft.id)
