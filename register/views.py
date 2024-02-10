from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})
