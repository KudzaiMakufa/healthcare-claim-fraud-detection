from django.urls import path
from dashboard import views
app_name = 'dashboard'
urlpatterns = [ 
    path('create', views.dashboard_index ,name="index"),
    path('libraries', views.dashboard_libraries ,name="libraries"),
    path('delete_claim/<int:librabry_id>', views.delete_claim , name="delete_claim"),
   
    

    
    


    
 
]