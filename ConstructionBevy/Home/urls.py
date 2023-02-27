from django.urls import path
from Home.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]