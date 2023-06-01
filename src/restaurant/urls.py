from django.urls import path
from .views import Dashboard, OrderDetails, menu_items

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
    path('menu/<int:restaurant_id>/', menu_items, name='menu_items'),
]
