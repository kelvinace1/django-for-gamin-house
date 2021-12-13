from django.contrib.auth import forms
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'account created for {username} ')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form':form})

