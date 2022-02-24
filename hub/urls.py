from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<int:pk>', views.room, name='rooms'),
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<int:pk>/', views.update_room, name='update-room'),
    path('delete-room/<int:pk>/', views.delete_room, name='delete-room'),
    path('delete-message/<int:pk>/', views.delete_message, name='delete-message'),
    path('update-message', views.update_message, name='update-message'),

    # user authentification
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.log_out, name='logout')
]
