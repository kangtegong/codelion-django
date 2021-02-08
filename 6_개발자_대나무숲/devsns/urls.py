from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('freehome/', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),

    path('login/', accounts_views.login, name='login'),    
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('', views.freehome, name='freehome'),
    path('freepostcreate', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),

    path('accounts/', include('allauth.urls')),

]
