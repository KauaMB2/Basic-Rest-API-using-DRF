from django.urls import path
from .views import ProductList, ProductDetail, getRoutes, deleteProduct, postProduct, putProduct

urlpatterns = [#Route list
    path('', getRoutes, name="RoutesList"),#Add one route
    path('products/', ProductList, name='ProductList'),#Add one route
    path('products/<int:pk>/', ProductDetail, name='ProductDetail'),#Add one route
    path('delete/<int:pk>/', deleteProduct, name="Delete Product"),
    path('post/', postProduct, name="Post product"),
    path('put/<int:pk>/', putProduct, name="Put data")
]
