from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("Home", views.Home, name='next'),
    path("login", views.login, name='login'),
    path("forgotpassword", views.forgotpassword, name='forgotpassword'),
    path("register", views.register, name='register'),
    path("changepassword", views.changepassword, name='changepassword'),
    path("voicecall", views.voicecall, name='voicecall'),
    path("videocall", views.videocall, name='videocall'),
    path("chat", views.chat, name='chat'),
    path("schedule", views.schedule, name='schedule'),
    path("search", views.search, name='search'),
    path("profile", views.profile, name='profile'),
    path("blogdetails", views.blogdetails, name='blogdetails'),
    path("blog", views.blog, name='blog'),
    path("menteedashboard", views.menteedashboard, name='menteedashboard'),
    path("booking", views.booking, name='booking'),
    path("appointment", views.appointments, name='appointments'),
    path("favourites", views.favourites, name='favourites'),
    path("profilesettings", views.profilesettings, name='profilesettings'),
    path("invoices", views.invoices, name='invoices'),
    path("review", views.review, name='review'),
    path("invoiceviews", views.invoiceviews, name='invoiceviews'),
    path("mapgrid", views.mapgrid, name='mapgrid'),
    path("maplist", views.maplist, name='maplist'),
    
]
