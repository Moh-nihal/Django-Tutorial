from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('nextpage',views.nextpage,name='nextpage'),
    path('register',views.register,name='register')
]
