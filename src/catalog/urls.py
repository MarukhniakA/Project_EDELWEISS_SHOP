from django.urls import path
from . import views
app_name = "catalog"

urlpatterns = [
    path('book/<int:pk>', views.BookView.as_view(), name="view-book"),
    path('book-add/', views.BookAddView.as_view(), name="add-book"),
    path('book-update/<int:pk>', views.BookUpdateView.as_view(), name="update-book"),
    path('book-delete/<int:pk>', views.BookDeleteView.as_view(), name="delete-book"),
    path('book-list/',views.BookListView.as_view(), name="list-book"),

]