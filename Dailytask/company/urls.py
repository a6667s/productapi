from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views 

urlpatterns = [
    path('catagory/', views.Categoryview.as_view()),
    path('catagory/<int:pk>/', views.CategoryDetail.as_view()),
    path('product/', views.Productview.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product-search/',views.ProductSearch.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)