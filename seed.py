# import os
# import django
# from datetime import timedelta
# from django.utils import timezone

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()

# from django.contrib.auth.models import User
# from nft.models import Category, Feature, FAQ, Team, Partner, NFT, NFTDetail

# def seed_data():
#     print("Clearing old data...")
#     NFTDetail.objects.all().delete()
#     NFT.objects.all().delete()
#     Partner.objects.all().delete()
#     Team.objects.all().delete()
#     FAQ.objects.all().delete()
#     Feature.objects.all().delete()
#     Category.objects.all().delete()
    
#     # Don't delete superusers if they exist, to prevent breaking admin access
#     User.objects.filter(is_superuser=False).delete()

#     print("Creating Users...")
#     u1, _ = User.objects.get_or_create(username="Richard")
#     u1.set_password("password123")
#     u1.save()
    
#     u2, _ = User.objects.get_or_create(username="Michael")
#     u2.set_password("password123")
#     u2.save()

#     print("Creating Categories...")
#     c1 = Category.objects.create(name="Digital Art")
#     c2 = Category.objects.create(name="Collectibles")

#     print("Creating Features (Stats)...")
#     Feature.objects.create(title="NFT's", value="23,400", icon="fa-rocket")
#     Feature.objects.create(title="Collections", value="8,000", icon="fa-wallet")
#     Feature.objects.create(title="Creators", value="3,400", icon="fa-users")
#     Feature.objects.create(title="Volume", value="521 B+", icon="fa-chart-line")

#     print("Creating FAQs...")
#     FAQ.objects.create(
#         question="What is an NFT marketplace?", 
#         answer="An NFT marketplace is a platform that allows users to buy, sell, and trade non-fungible tokens (NFTs)."
#     )
#     FAQ.objects.create(
#         question="How does buying an NFT work?", 
#         answer="Buying an NFT requires a crypto wallet and some cryptocurrency. You can browse our marketplace, bid or buy instantly."
#     )
#     FAQ.objects.create(
#         question="What are the benefits of owning an NFT?", 
#         answer="Owning an NFT provides proof of ownership, access to exclusive communities, and more."
#     )

#     print("Creating Team...")
#     Team.objects.create(name="Floyd Miles", position="Designer")
#     Team.objects.create(name="Eleanor Pena", position="VA Designer")
#     Team.objects.create(name="Kim Dorka", position="UX Specialist")
#     Team.objects.create(name="William Lake", position="Software Engineer")

#     print("Creating Partners...")
#     for partner_name in ["LOGOTYPE", "BOGO", "TRUSTY", "FINANCE", "GALAXY"]:
#         Partner.objects.create(name=partner_name)

#     print("Creating NFTs and Details...")
#     nft1 = NFT.objects.create(
#         title="ExBoot #1", 
#         creator=u1, 
#         price=3.421, 
#         category=c1, 
#         end_time=timezone.now() + timedelta(hours=2)
#     )
#     NFTDetail.objects.create(
#         nft=nft1, 
#         description="We would like to present you The Exboot 3D – Watching you~ a digital collectible that utilizes blockchain technology to prove authenticity and scarcity.", 
#         collection="Robot Series"
#     )

#     nft2 = NFT.objects.create(
#         title="ExBoot #2", 
#         creator=u2, 
#         price=4.120, 
#         category=c1, 
#         end_time=timezone.now() + timedelta(hours=4)
#     )
#     NFTDetail.objects.create(
#         nft=nft2, 
#         description="The second edition of the Exboot series, continuing our interstellar blockchain journey.", 
#         collection="Astronaut Series"
#     )

#     nft3 = NFT.objects.create(
#         title="Epic Item #3", 
#         creator=u1, 
#         price=1.350, 
#         category=c2
#     )
#     NFTDetail.objects.create(
#         nft=nft3, 
#         description="A really epic item created for our exclusive collectible hunters.", 
#         collection="Epic Collectors"
#     )
    
#     nft4 = NFT.objects.create(
#         title="Epic Item #4", 
#         creator=u2, 
#         price=2.000, 
#         category=c2,
#         end_time=timezone.now() + timedelta(days=2)
#     )
#     NFTDetail.objects.create(
#         nft=nft4, 
#         description="Another epic test item.", 
#         collection="Epic Collectors"
#     )

#     print("Data successfully seeded! ✨")

# if __name__ == "__main__":
#     seed_data()
