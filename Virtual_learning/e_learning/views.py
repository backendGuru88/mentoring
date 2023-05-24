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
def search(request):
    return render(request, 'search.html')
def profile(request):
    return render(request, 'profile.html')
def blogdetails(request):
    return render(request, 'blog-details.html')
def blog(request):
    return render(request, 'blog-list.html')
def menteedashboard(request):
    return render(request, 'dashboard-mentee.html')
def booking(request):
    return render(request, 'booking.html')
def appointments(request):
    return render(request, 'appointments.html')
def favourites(request):
    return render(request, 'favourites.html')
def review(request):
    return render(request, 'reviews.html')
def profilesettings(request):
    return render(request, 'profile-settings.html')
def invoices(request):
    return render(request, 'invoices.html')
def invoiceviews(request):
    return render(request, 'invoice-views.html')
def mapgrid(request):
    return render(request, 'map-grid.html')
def maplist(request):
    return render(request, 'map-list.html')