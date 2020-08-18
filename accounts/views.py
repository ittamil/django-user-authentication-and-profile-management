from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()        

    return render(request,'registration/register.html',{'form':form}) 


def LoginView(request):
    return render(request,'login.html')

@login_required
def profile(request):
    return render(request,'profile.html')
