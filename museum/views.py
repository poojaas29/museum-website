from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *


# Create your views here.

def Home(request):
    return render(request, 'home.html')


def About(request):c
    return render(request, 'about.html')


def Gallery(request):
    return render(request, 'gallery.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Customer_Profile(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        us = request.POST['username']
        pd = request.POST['password']
        ad = request.POST['address']
        nat = request.POST['nationality']
        d = request.POST['dob']
        ag = request.POST['age']
        c = request.POST['contact']
        try:
            user = User.objects.create_user(
                username=us, password=pd, first_name=fn, last_name=ln)
            Customers.objects.create(
                user=user, nationality=nat, dob=d, age=ag, contact=c, address=ad)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_profile.html', d)


def Visitor_Details(request):
    if not request.user.is_authenticated:
        return redirect('login')
    visitor = Customers.objects.all()
    d = {'visitor': visitor}
    return render(request, 'visitor_details.html', d)


def View_Booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    booked = Booking_Details.objects.all()
    d = {'booked': booked}
    return render(request, 'view_booking.html', d)


def Book_Ticket(request):
    error = ""
    if not request.user:
        return redirect('user_login')
    ticket = Booking_Details.objects.all()
    if request.method == "POST":
        dat = request.POST['date']
        t = request.POST['time']
        no = request.POST['number']
        ua = User.objects.filter(username=request.user.username).first()
        try:
            Booking_Details.objects.create(
                user=ua, date=dat, time=t, number=no)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'book_ticket.html', d)


def User_Login(request):
    error = ""
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = authenticate(username=un, password=pw)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_login.html', d)
