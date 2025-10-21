from django.urls import path

from . import views

urlpatterns = [

    

    path('login/', views.login),



    # ------------Homepage-----------------#

    path('', views.home, name=''),  # Default home page


    # ------------Register a User-----------------#

    path('register', views.register, name="register"),


    # ------------Login a User-----------------#


    path('my-login', views.my_login, name="my-login"),
 

 

    # ------------Dashboard page-----------------#

    
    path('dashboard', views.dashboard, name="dashboard"),


    # ------------Profile Management page-----------------#

    
    path('profile-management', views.profile_management, name="profile-management"),


    # ------------Delete accont-----------------#

    path('delete-account', views.deleteAccount, name="delete-account"),


    # ------------CREATE A TASK-----------------#



    path('create-task', views.createTask, name="create-task"),


    # ------------READ A TASK-----------------#

     

    path('view-tasks', views.viewTask, name="view-tasks"),


    # ------------UPDATE TASK-----------------#


    path('update-task/<str:pk>/', views.updateTask, name="update-task"),


    # ------------DELETE TASK-----------------#


    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),

   

    # ------------Logout a User-----------------#


    path('user-logout', views.user_logout, name="user-logout"),
 

    

]








