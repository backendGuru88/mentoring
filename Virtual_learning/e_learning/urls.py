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
    
]
