"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import Home, Signup, Signout, Signin, About, Contact, ShopS, Shop, Table, Forgot, Chart, Index2, BasicE
from api import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('about/',About.as_view(),name='about'),
    path('contact/',Contact.as_view(),name='contact'),
    path('shops/',ShopS.as_view(),name='shops'),
    path('shop/',Shop.as_view(),name='shop'),
    #path('signin/',Signin.as_view(),name='signin'),
    #path('signup/',Signup.as_view(),name='signup'),
    path('signin/',Signin.as_view(),name='signin'),
    path('signup/',Signup.as_view(), name='signup'),
    path('logout/',Signout.as_view(), name='logout'),
    path('forgot/',Forgot.as_view(), name='forgot'),
    path('table/',Table.as_view(), name='table'),
    path('index2/',Index2.as_view(), name='index2'),
    path('chartjs/',Chart.as_view(), name='chartjs'),
    path('basic_elements/',BasicE.as_view(), name='basic_elements'),
    #path('acceso/',views.acceso, name='acceso'),  ,
    path('enviar_correo/<str:asunto>/<str:correo>/<str:usuario>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
    
      
    
]
