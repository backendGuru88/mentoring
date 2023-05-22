from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def Home(request):
    return render(request , 'index-two.html')
def login(request):
    return render(request , 'login.html')
def forgotpassword(request):
    return render(request,'forgot-password.html')
def register(request):
    return render(request, 'register.html')
def changepassword(request):
    return render(request, 'change-password.html')
def voicecall(request):
    return render(request, 'voice-call.html')
def videocall(request):
    return render(request, 'video-call.html')
def chat(request):
    return render(request, 'chat.html')
def schedule(request):
    return render(request, 'schedule-timings.html')