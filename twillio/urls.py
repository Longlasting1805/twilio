from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.handle_incoming_call, name='incoming-call'),
]