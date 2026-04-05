from django.urls import path
from . import views

app_name = 'nft'

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('detail/', views.detail, name='detail'),
    path('detail/<int:pk>/', views.detail, name='detail_pk'),
    path('become-artist/', views.become_artist, name='become_artist'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('purchase/<int:pk>/', views.purchase_nft, name='purchase'),
]
