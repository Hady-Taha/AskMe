from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.register ,name='register'),
   
    path('login/', views.loginv ,name='login'),
    
    path('profile/<slug:slug>',views.profile,name='profile'),
    
    path('logout/', views.logoutv ,name='logout'),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)