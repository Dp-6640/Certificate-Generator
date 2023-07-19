from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
    path('customize_certificate/<int:certificate_id>/', views.customize_certificate, name='customize_certificate'),
]
