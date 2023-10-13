from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('category/<slug:val>', views.CategoryView.as_view(), name= 'category'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name= 'product-detail'),

    #authentication
    path('registration/', views.CustomerRegView.as_view(), name = 'registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name= 'main/login.html', authentication_form=LoginForm), name='login'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
