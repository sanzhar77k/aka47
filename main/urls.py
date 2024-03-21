from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog_page, name='blog_page'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('interior', views.interior_page, name='interior_page'),
    path('interior/<int:interior_id>/', views.interior_detail, name='interior_detail'),
    path('exterior', views.exterior_page, name='exterior_page'),
    path('exterior/<int:exterior_id>/', views.exterior_detail, name='exterior_detail'),
    path('blog/<int:blog_id>/comment/', views.add_comment, name='add_comment'),
]
