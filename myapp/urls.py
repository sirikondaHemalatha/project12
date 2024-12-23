from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',sheryians,name='sheryians'),
    path('home/',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('frontend/',frontend,name='frontend'),
    path('backend/',backend,name='backend'),
    path('aptitude/',aptitude,name='aptitude'),
    path('java/',java,name='java')
]