from django.urls import path

from  .views import DishesCreateView, DishesListView, DishesDetailView, CategoryListCreateView, CategoryDetailView, OrderListCreateView, OrderDetailView   

urlpatterns = [
    path('dishes/', DishesListView.as_view(), name='dishes-list'),
    path('dishes/create/', DishesCreateView.as_view(), name='dishes-create'),
    path('dishes/<int:pk>/', DishesDetailView.as_view(), name='dishes-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
        
]   