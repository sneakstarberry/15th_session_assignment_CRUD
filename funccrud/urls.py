from django.urls import path
from . import views

urlpatterns = [

    path('', views.read, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name= 'logout'),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
]