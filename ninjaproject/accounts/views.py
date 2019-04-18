from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from  django.contrib.auth import login
import re 

def sign_up(request):
    if request.method == "POST":
       form = UserCreationForm(request.POST)

       print('request===>', request)
       print('request===>')
       print('form ===>', list(request.POST.values()))
       print('form ===>', list(request.POST.keys()))
  
    #    ri = re.findall(r"username=\w+", str(request.body))
    #    print('ri===>',ri[0])
       if form.is_valid():
          user = form.save()          
          login(request,user)
          return redirect('http://localhost:8000/article/')
 
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})


def loginView(request):
    if request.method == "POST":
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
          user = form.get_user()
          login(request,user)
          return redirect('http://localhost:8000/article/')
          
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})
