from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="blogs"),
    path('<int:id>',views.detail, name="detail"),
    path('search',views.search, name="search"),
    path('newblog',views.newblog, name="newblog"),
]