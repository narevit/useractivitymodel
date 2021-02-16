from django.conf.urls import include,url
from . import views
app_name = 'login'

urlpatterns=[
    url(r'^register$',views.register,name ='register'),
    url(r'^registersuccess$',views.registersuccess,name ='registersuccess'),

    url(r'^login$',views.login,name ='login'),
    url(r'^loginsuccess$',views.loginsuccess,name ='loginsuccess'),

    url(r'^dashboard$',views.dashboard,name ='dashboard'),

    url(r'^logout$',views.logout,name ='logout'),
]

