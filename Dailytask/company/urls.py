from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from company import views

urlpatterns = [
    path('catagory/', views.Categoryview.as_view()),
    path('product/', views.Productview.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    
   
]

urlpatterns = format_suffix_patterns(urlpatterns)