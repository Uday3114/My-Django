from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('login',views.user_login,name='login'),
    path('logout', views.user_logout,name='logout'),
    path('show', views.show, name = 'show'),
    path('edit/<int:pk>', views.update, name = 'update'),
    path('delete/<int:pk>', views.destroy, name = 'destroy'),
]