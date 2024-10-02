from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from scrap_app.models import UserProfile,Category,Scrap,Wishlist,Review,Bids


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
class LoginForms(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserprofileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",)

class CategoryForm(forms.ModelForm):
     class Meta:
        model=Category
        fields="__all__"

class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=("user",)
        
class WishlistForm(forms.ModelForm):
        class Meta:
            model=Wishlist
            fields="__all__"

class ReviewForm(forms.ModelForm):
        class Meta:
            model=Review
            fields="__all__"

class BidsForm(forms.ModelForm):
        class Meta:
            model=Bids
            fields="__all__"
