"""
URL configuration for scrapbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scrap_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.SignUpView.as_view(),name="signup"),
    path("",views.signInView.as_view(),name="signin"),
    path("scrapbox/signout", views.signoutView.as_view(),name="signout"), 
    path("scrapbox/index", views.IndexView.as_view(),name="index"),
    path("profile/<int:pk>/change", views.ProfileUpdateView.as_view(),name="profile_add"),
    path("profile/<int:pk>", views.ProfileDetailView.as_view(), name="profile"),
    path("scrapbox/scrap/add", views.ScrapAddView.as_view(),name="scrap_add"),
    path("scrapbox/scrap/category", views.CategoryAddView.as_view(), name="category"),
    path("scrapbox/scrap/<int:pk>", views.ScrapDetailView.as_view(), name="scrap-detail"),
    path("scrapbox/<int:pk>/change", views.ScrapUpdateView.as_view(),name="scrap-update"),
    path("scrapbox/<int:pk>/remove", views.ScrapDeteteView.as_view(),name="scrap-delete"),
    path('profiles/all',views.ProfileListView.as_view(),name="profile_list"),
    path("scrap/<int:pk>/details/", views.ScrapDetailView.as_view(), name="product-details"),
    path('scrapbox/product/',views.PostAddView.as_view(),name="post_product"),
    path('scrapbox/review/',views.ReviewAddView.as_view(),name="review"),
    path("scrapbox/bids", views.BidsAddView.as_view(), name="bids"),
    path("scrapbox/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
    path('scrapbox/wishlist/',views.WishlistAddView.as_view(),name="favorite"),
    path("scrapbox/<int:pk>/wishlist", views.WishlistDetailView.as_view(),name="wishlist"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

