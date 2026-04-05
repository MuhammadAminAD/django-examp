from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="FontAwesome icon class (e.g. fa-rocket)")
    value = models.CharField(max_length=50, blank=True, null=True, help_text="For stats, e.g. '23,400'")

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=100, default="General")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class NFT(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_nfts')
    image = models.ImageField(upload_to='nfts/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NFTDetail(models.Model):
    nft = models.OneToOneField(NFT, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()
    collection = models.CharField(max_length=100)
    minted_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Details of {self.nft.title}"
