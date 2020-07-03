from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    # new users registration already provieded by django
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # is imput data valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # flash message saying it was succesful
            messages.success(request, f'Account Created For {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
