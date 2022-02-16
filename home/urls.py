from django.urls import path
from home import views
app_name = 'home'
urlpatterns = [ 
    
    path('', views.home_login , name="login"),
    path('logout', views.home_logout ,name="logout"),
    path('profile', views.home_profile ,name="profile"),


]
