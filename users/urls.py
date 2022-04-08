from django.urls import path

from users import views

urlpatterns = [
    path('users/<int:pk>/', views.user_detail, name='detail_users'),
    path('users/', views.user_list, name='all_users'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
