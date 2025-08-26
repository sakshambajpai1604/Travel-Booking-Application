from django.shortcuts import render


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

# Profile update form
class ProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('profile')
	else:
		form = UserCreationForm()
	return render(request, 'core/register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('profile')
		else:
			messages.error(request, 'Invalid username or password.')
	else:
		form = AuthenticationForm()
	return render(request, 'core/login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('login')

@login_required
def profile_view(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Profile updated!')
			return redirect('profile')
	else:
		form = ProfileForm(instance=request.user)
	return render(request, 'core/profile.html', {'form': form})
