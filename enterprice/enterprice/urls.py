"""enterprice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from home.views import index, authenticate_user
from store_review.views import view_purchases, write_review, submit_review, view_store_profile, delete_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('login/authenticate/', authenticate_user),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('my-purchases/', view_purchases, name='my-purchases'),
    path('write-review/<int:purchase_id>', write_review, name='write-review'),
    path('submit-review', submit_review, name='submit-review'),
    path('store/<str:store_username>', view_store_profile, name='view-store-profile'),
    path('delete-review/<int:purchase_id>', delete_review, name='delete-review'),
]
