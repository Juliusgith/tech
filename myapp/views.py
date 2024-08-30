# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def success(request):
    return render(request, 'success.html')

from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

def services(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after submission
    else:
        form = CommentForm()
    return render(request, 'services.html', {'form': form})
