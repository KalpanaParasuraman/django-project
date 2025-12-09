from django.urls import path
from . import views

urlpatterns = [
    path('session/', views.counter_view, name='counter'),
]
