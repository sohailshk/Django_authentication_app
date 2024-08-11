from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_view, name='register'), #for url's to get icluded we first define url present in app
    path('login/',views.login_view, name='login'),  #then we define what that url does from views 
    path('logout/',views.logout_view, name='logout'),#to use it in templates without implcitly writing the whole thing
    path('dashboard/',views.dashboard, name='dashboard')
]

