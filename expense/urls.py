from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name="index"),
    path('surge', views.second, name="second" ),
    path('post', csrf_exempt(views.post), name="post"),
    path('passw', views.passw, name="passw"),
     path('activate/<uidb64>/<token>', views.tokin, name='activate'),
     path('login', views.login, name="login"),
     path('logout', views.logout, name="logout")
]
