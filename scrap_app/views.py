from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import FormView,CreateView,TemplateView,View,UpdateView,DetailView,ListView
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout

from scrap_app.models import UserProfile,Scrap,Review,Wishlist,Bids
from scrap_app.forms import RegisterForm,LoginForms,UserprofileForm,CategoryForm,ScrapForm,ReviewForm,WishlistForm,BidsForm
# from scrap_app.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages
from django import forms



decs=[login_required,never_cache]


class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegisterForm

    def get_success_url(self):
        return reverse("signin")

class signInView(FormView):
    template_name="login.html"
    form_class=LoginForms

    def post(self,request,*args,**kwargs):
        forms=LoginForms(request.POST)
        if forms.is_valid():
            uname=forms.cleaned_data.get("username")
            pwd=forms.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:
                login(request,user_object)
                print("successfully.............")
                return redirect("index")
        print("failed")
        messages.error(request,"failed to login invalid credentials")
        return render(request ,"login.html",{"form":forms})

@method_decorator(decs,name="dispatch")
class IndexView(ListView):
    template_name="index.html"
    form_class=ScrapForm
    model=Scrap
    context_object_name="data"

@method_decorator(decs,name="dispatch")
class signoutView(View):
    def get(self,request,*args,**kwargs):
         logout(request)
         return redirect("signin")
    
@method_decorator(decs,name="dispatch")
class ProfileUpdateView(UpdateView):
     template_name='profile_add.html'
     form_class=UserprofileForm
     model=UserProfile 

     def get_success_url(self):
          return reverse("index")

@method_decorator(decs,name="dispatch")
class ProfileDetailView(DetailView):
     template_name='profile.html'
     model=UserProfile
     context_object_name="data"
     def get_success_url(self):
        return reverse("index")

@method_decorator(decs,name="dispatch")
class ProfileListView(View):
    def get(self,request,*args,**kwargs):
        qs=UserProfile.objects.all()
        return render(request,"profile_list.html",{"data":qs})


@method_decorator(decs,name="dispatch")
class CategoryAddView(CreateView):
    template_name='category.html'
    form_class=CategoryForm
    def get_success_url(self):
        return reverse("index")

@method_decorator(decs,name="dispatch")
class ScrapAddView(View):
    def get(self, request,*args, **kwargs):
        form_class=ScrapForm
        model=Scrap
        context_object_name="scrapdata"
        return render(request,"scrap_add.html",{'form': form})
    def post(self, request,*args, **kwargs):
        form=ScrapForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("index")
        else:
            return render(request, "scrap_add.html",{'form': form})

@method_decorator (decs,name="dispatch")
class ScrapDeteteView(DetailView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        Scrap.objects.get(id=id).delete()
        return redirect("index")

@method_decorator (decs, name="dispatch")
class ScrapUpdateView(UpdateView):
    template_name="scrap_update.html"
    form_class=ScrapForm
    model=Scrap

    def get_success_url(self):
        return reverse("index")

@method_decorator (decs, name="dispatch")
class ScrapDetailView(DetailView):
    template_name="product_details.html"
    model=Scrap
    context_object_name="data"
    
@method_decorator (decs, name="dispatch")
class ReviewDetailView(DetailView):
    template_name="review_detail.html"
    model=Review
    context_object_name="data"


@method_decorator (decs, name="dispatch")
class PostAddView(View):
    def get(self, request,*args, **kwargs):
        form_class=ScrapForm
        return render(request,"post_product.html",{'form': forms})
    def post(self, request,*args, **kwargs):
        forms=ScrapForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.instance.user=request.user
            forms.save()
            return redirect("index")
        else:
            return render(request, "post_product.html",{'form': forms})
            
@method_decorator (decs, name="dispatch")
class ScrapOrderView(View):
    template_name="product_order.html"
    form_class=LoginForms

    def post(self,request,*args,**kwargs):
        forms=LoginForms(request.POST)
        if forms.is_valid():
            uname=forms.cleaned_data.get("username")
            pwd=forms.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:
                login(request,user_object)
                print("successfully.............")
                return redirect("index")
        print("failed")
        messages.error(request,"failed to login invalid credentials")
        return render(request ,"login.html",{"form":forms})


@method_decorator (decs, name="dispatch")
class ReviewAddView(View):
    def get(self, request,*args, **kwargs):
        form_class=ReviewForm
        context_object_name="data"
        return render(request,"review.html",{'form': forms})
    def post(self, request,*args, **kwargs):
        forms=ReviewForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.instance.user=request.user
            forms.save()
            return redirect("index")
        else:
            return render(request, "review.html",{'form': forms})

            


@method_decorator (decs, name="dispatch")
class BidsAddView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Bids.objects.all().filter(user=request.user)
        return render(request,"bids.html",{"data":qs})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Bids.objects.get(id=id)
        action=request.POST.get("action")
        if action=="remove":
            Bids.scrap.remove(qs)
        return redirect("bids")


@method_decorator (decs, name="dispatch")
class WishlistAddView(View):
    def get(self, request,*args, **kwargs):
        form_class=WishlistForm
        return render(request,"favorite.html",{'form': forms})
    def post(self, request,*args, **kwargs):
        forms=WishlistForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.instance.user=request.user
            forms.save()
            return redirect("index")
        else:
            return render(request, "favorite.html",{'form': forms})

@method_decorator (decs, name="dispatch")
class WishlistDetailView(DetailView):
    template_name="wishlist.html"
    model=Wishlist
    context_object_name="data"



