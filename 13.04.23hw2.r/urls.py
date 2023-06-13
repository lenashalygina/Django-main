from django.urls import path, include
from products.views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
