from django.urls import path
from .views import mail ,success



urlpatterns = [
    path('',mail,name='mail'),  
    path("success", success, name="success"),
]
