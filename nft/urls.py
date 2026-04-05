from django.urls import path
from . import views

app_name = 'nft'

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('detail/', views.detail, name='detail'),
    path('become-artist/', views.become_artist, name='become_artist'),
    path('faq/', views.faq, name='faq'),
]
