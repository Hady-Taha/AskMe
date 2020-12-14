from django.urls import path
from . import views
urlpatterns = [
    path('inbox/<slug:slug>',views.inbox,name='inbox'),
    path('delete/<int:id>',views.deletem,name='delete')
]