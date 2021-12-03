from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
	path('', views.BooksModelView.as_view(), name='index'),
	path('book/', views.BooksList.as_view(), name='book_list'),
	path('author/', views.BooksAuthorList.as_view(), name='author_list'),
	path('publisher/', views.BooksPublisherList.as_view(), name='publisher_list'),
	path('book/<int:pk>/', views.BooksDetail.as_view(), name='book_detail'),
	path('publisher/<int:pk>/', views.BooksDetail.as_view(), name='publisher_detail'),
]
