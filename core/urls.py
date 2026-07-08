from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('signup/', views.signup_view, name='signup'),
    path('employer-signup/', views.employeer_signup, name='employer-signup'),
    path('employer-login/', views.employeer_login, name='employer-login'),
    path('applicant-dashboard/', views.applicant_dashboard, name='applicant-dashboard'),
    path('employer-dashboard/', views.employer_dashboard, name='employer-dashboard'),
    path('job-list/', views.employer_job_list, name='job-list'),
    path('job-pots/', views.employer_job_post, name='job-post'),
    path("employer/job/<int:job_id>/toggle/", views.toggle_job_status, name="toggle-job-status"),
    path('employer-logout/', views.employee_logout, name='employer-log')
]
