from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateBook, name='createbook'),
    path('author/', views.CreateAuthor, name='author'),
    path('', views.listBook, name='booklist'),
    path('details/<int:book_id>/', views.detailView, name='details'),
    path('delete/<int:book_id>/', views.deleteView, name='delete'),
    path('update/<int:book_id>/', views.updateBook, name='update'),
    path('index', views.index),
    path('search/', views.SearchBook, name='search'),

]
