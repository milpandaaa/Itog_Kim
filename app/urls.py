from django.contrib import admin
from django.urls import path, include

from app.views import *

urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', reader_all, name="home_url"),
    path('newBook', newBook, name="newBook"),
    path('newReader', newReader, name="newReader"),
    path('', menu, name="menu"),
    path('card/<int:reader_id>/', card, name="card"),
    path('reader/<int:reader_id>/', reader, name="reader"),
    path('books', books, name="books"),
    path('delete/<int:book_id>/', delete, name="delete"),
]