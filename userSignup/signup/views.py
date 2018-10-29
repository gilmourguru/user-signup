from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from userSignup.signup.forms import SignUpForm
import ctypes


# @login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
@csrf_exempt
def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home.html', context=None)
    else:
        return Mbox('Authentication Error: ', 'Your username/password combination is not valid.', 0)

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)