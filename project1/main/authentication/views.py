from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUserCreationForm
from .forms import UpdateUserForm ,UpdatepasswordrForm


# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('home')
        else:
            massge = "Something went Wrong in your Login ,Try Again "
            return render(request,'authentication/login.html',{'massge':massge})
    return render(request,'authentication/login.html')


def signup_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Please fill in the form correctly.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


@login_required
def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('update_user')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'authentication/update_user.html', {'form': form})


@login_required
def update_password(request):
    if request.method == 'POST':
        form = UpdatepasswordrForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been updated successfully. Please log in again to continue.")
            return redirect('login')
        else:
            messages.error(request, "Please fill in the form correctly.")
    else:
        form = UpdatepasswordrForm(request.user)
    return render(request, 'authentication/update_password.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been loged out successfully. Please log in again to continue.")
    return redirect('login')