from django.urls import path
from .views import  base , index
urlpatterns = [
      path("enter" , base ),
      path("index" , index)
]