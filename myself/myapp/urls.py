from django.urls import path
from .views import *

urlpatterns = [
path('', home, name="call-home"),
path('about/', about, name = " call-about")

]