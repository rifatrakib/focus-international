from django.urls import path
from programs import views

app_name = 'programs'
urlpatterns = [
    path('', views.get_programs, name='programs-summary'),
]
