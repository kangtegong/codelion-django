from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('detail1/', views.detail1, name='detail1'),
    path('detail2/', views.detail2, name='detail2'),
    path('detail3/', views.detail3, name='detail3'),
    path('detail4/', views.detail4, name='detail4'),
    path('detail5/', views.detail5, name='detail5'),
    path('detail6/', views.detail6, name='detail6'),
    path('detail7/', views.detail7, name='detail7'),
    path('detail8/', views.detail8, name='detail8'),
    path('detail9/', views.detail9, name='detail9'),
]
