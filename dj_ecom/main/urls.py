from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('category/<slug:val>', views.CategoryView.as_view(), name= 'category'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name= 'product-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
