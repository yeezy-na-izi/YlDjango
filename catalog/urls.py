from django.urls import path
from catalog import views

urlpatterns = [
    path('<pk>/', views.item_detail, name='item_detail'),
    path('', views.item_list, name='all_items'),
]
