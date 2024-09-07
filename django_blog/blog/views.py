from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login") 
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form":form})

@login_required
def profile(request):
    return render(request, "blog/profile.html")

