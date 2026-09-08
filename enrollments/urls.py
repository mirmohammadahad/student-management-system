from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('ledger/', views.enrollment_ledger, name='ledger'),
    path('add/', views.enrollment_create, name='enrollment_create'),
    path('<int:pk>/edit/', views.enrollment_update, name='enrollment_update'),
    path('<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
    path('<int:pk>/update-status-ajax/', views.update_enrollment_status_ajax, name='update_status_ajax'),
    path('live-search/', views.live_search_enrollments, name='live_search'),
]