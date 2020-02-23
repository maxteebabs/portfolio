
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug>', views.details, name='show_project'),
    path('contact', views.contact, name='contact'),
]
