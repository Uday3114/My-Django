from django.urls import path
from . import views
urlpatterns=[
    path('',views.showformdata,name='formapp'),
    path('mod',views.mydb,name='mydb'),
]