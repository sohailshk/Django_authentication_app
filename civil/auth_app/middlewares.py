# taaki user ek page se dusre page without login naa jaa sake login would be the only option
from django.shortcuts import  redirect
# below doesn't allow unauthenticated user to get access to dashboard through url
# auth is a decorator function so that whichever view we want to apply authentication we can write @auth actual code is in wrapped_view
#auth is decorater and wrapped_view is actually the decorated function it is main task performing function
def auth(view_function):  #auth function checks if user is autenticated befor allowing him to visit view argument
    def wrapped_view(request, *arg, **kwargs): #*arg and **kwargs tells that we can pass any arguments which right now we don't know but can be added afterwards
        if request.user.is_authenticated == False: 
            return redirect('login')
        return view_function(request,*arg,**kwargs) #we passes args to view function so that if any extra args was added in view it should show
    return wrapped_view

#guest decorator banda logged in hai and woh phirse login page pe na jaa paye
def guest(view_function):  # auth function checks if user is autenticated befor allowing him to visit view argument
    def wrapped_view(request, *arg, **kwargs):  # *arg and **kwargs tells that we can pass any arguments which right now we don't know but can be added afterwards
        if request.user.is_authenticated == True: 
            return redirect('dashboard')
        return view_function(request, *arg, **kwargs)  # we passes args to view function so that if any extra args was added in view it should show

    return wrapped_view
    
