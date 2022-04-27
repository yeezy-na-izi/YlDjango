from django.urls import path

from homepage import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
]
