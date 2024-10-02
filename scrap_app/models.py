from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profilepic",null=True,blank=True)

    def _str_(self):
        return self.user.username

def create_profile(sender,created,instance,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("created")

    
    
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Scrap(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_scrap")
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    scrap_image=models.ImageField(upload_to="scrappics")
    condition=models.CharField(max_length=200,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    status_option=(
        ("Sold","sold"),
        ("Available","available")
    )
    status=models.CharField(max_length=200,choices=status_option,default="Available")

    def _str_(self):
        return self.name
    
class Wishlist(models.Model):
    scrap=models.ManyToManyField(Scrap,related_name="wished_scrap")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_wish")
    created_date=models.DateTimeField(auto_now_add=True)

class Bids(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_bids")
    scrap=models.ForeignKey(Scrap,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    bids_options=(
        ("Pending","pending"),
        ("Accept","accept"),
        ("Reject","reject"),
    )
    status=models.CharField(max_length=200,choices=bids_options,default="Pending")

    def _str_(self):
        return self.amount
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_review")
    scrap=models.ForeignKey(Scrap,on_delete=models.CASCADE,related_name="scrap_review")
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()

    def _str_(self):
        return self.comment


post_save.connect(create_profile,sender=User)
