from django.urls import path

from catalog import views

urlpatterns = [
    path('<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('', views.ItemList.as_view(), name='all_items'),
]
