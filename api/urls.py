from django.urls import path
from .views import main, register

urlpatterns = [
    path("home", main),
    path("register", register)

]
