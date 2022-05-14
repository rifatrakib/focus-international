from django.urls import path
from programs import views

app_name = 'programs'
urlpatterns = [
    path('', views.get_programs_summary, name='programs-summary'),
    path('<int:program_id>/', views.get_program_details, name='program-details'),
]
