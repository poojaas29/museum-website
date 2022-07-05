"""Museum_Mgt_final URL Configuration

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
from museum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', About, name='about'),
    path('', Home, name='home'),
    path('admin_login', Login, name='login'),
    path('user_profile', Customer_Profile, name='user_profile'),
    path('visitor_details', Visitor_Details, name='visitor_details'),
    path('view_booking', View_Booking, name='view_booking'),
    path('book_ticket', Book_Ticket, name='book_ticket'),
    path('user_login', User_Login, name='user_login'),
    path('logout', Logout_admin, name='logout'),
    path('gallery', Gallery, name='gallery'),

]
