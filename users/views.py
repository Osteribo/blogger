from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    # new users registration already provieded by django
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # is imput data valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # flash message saying it was succesful
            messages.success(request, f'Your account has been created! You can now login {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
