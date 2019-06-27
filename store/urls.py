from django.urls import path
from . import views
from store.views import *

app_name = "store"

urlpatterns = [
    path('',views.index,name="index"),
    path('books/',bookListView,name="book-list"),
    path('book/<int:pk>/',Detailview.as_view(),name='book-detail' ),
    path('books/loaned/',viewLoanedBooks,name="view-loaned"),
    path('books/loan/',loanBookView,name="loan-book"),
    path('books/return',returnBookView,name="return-book"),
    path('register/', register, name="register"),
    path('logout/', logout_req, name="logout"),
    path("login/", login_req, name="login"),

]
