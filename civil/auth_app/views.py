from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth  import login, logout
from .middlewares import auth,guest

@guest
def register_view(request): #we write request so we can get access to all the views info whenever we want
    if request.method == 'POST':  # user has submitted form POST
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)  # yeh django ka bult in login hai
            return redirect('dashboard')
    else:
        initial_data={'username':'','password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form}) #first argument mai request that we need
                                                                    # 2 mai joh page url return karna haiwoh 
                                                                    # 3 arg mai dictionary format mai return coz we
                                                                    #want to access it in templeate
def logout_view(request):
    logout(request)
    return redirect('login')

@guest
def login_view(request):
    if request.method == 'POST':  # user has submitted form POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() #server pe jakar user ki details lelo
            login(request,user)  # yeh django ka bult in login hai
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form':form})

@auth
def dashboard(request):
    return render(request,'dashboard.html')
