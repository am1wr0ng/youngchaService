"""youngchaproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accapp import views as accview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',accview.home, name='home'), #로그인 전 홈화면 

    path('login/',accview.login,name='login'),
    path('main_home/',accview.login_after,name='login_after'), #로그인 후 홈화면  
    path('signup/',accview.signup,name='signup'),
]
