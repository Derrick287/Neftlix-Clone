from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def loginPage(request):
    return render(request, 'core/login.html')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration.')
    return render(request, 'core/signup.html')

def userProfile(request):
    return render(request, 'core/user_profile.html')

def movieDetails(request):
    return render(request, 'core/movie_details.html')

def movieList(request):
    return render(request, 'core/movie_list.html')