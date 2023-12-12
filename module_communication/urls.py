from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'information', views.InformationViewSet, basename='information')
router.register(r'event', views.EventViewSet, basename='event')
router.register(r'group', views.GroupViewSet, basename='group')


urlpatterns = [
    path('participants_count/<int:event_id>/', views.participants_count, name='participants_count'),
    path('participate_event/<int:event_id>/<int:student_id>/<str:start_hours>/<str:end_hours>/<int:amount>/', views.participate_event, name='participate_event'),
    path('last_discussion_message/<int:sender_id>/<int:receiver_id>/', views.last_discussion_message, name='last_discussion_message'),
    path('last_group_message/<int:student_id>/<int:group_id>/', views.last_group_message, name='last_group_message'),
    path('all_group_messages/<int:student_id>/', views.all_group_messages, name='all_group_messages'),
    path('all_student_messages/<int:sender_id>/<int:receiver_id>/', views.all_student_messages, name='all_student_messages'),
]

urlpatterns += router.urls  # Ajoute les URL générées par DefaultRouter
