from django.urls import path

from about import views


urlpatterns = [
    path('', views.DescriptionView.as_view(), name='about'),
]
