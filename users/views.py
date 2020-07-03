from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    # new users registration already provieded by django
    form = UserCreationForm()
    return render(request, 'users/register.html', {'from': form})