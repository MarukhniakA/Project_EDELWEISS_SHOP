from django.urls import path
from . import views
app_name = "spravochniki"

urlpatterns = [
    path('author/<int:pk>', views.AuthorView.as_view(), name="view-author"),
    path('author-add/', views.AuthorAddView.as_view(), name="add-author"),
    path('author-update/<int:pk>', views.AuthorUpdateView.as_view(), name="update-author"),
    path('author-delete/<int:pk>', views.AuthorDeleteView.as_view(), name="delete-author"),
    path('author-list/',views.AuthorListView.as_view(), name="list-author"),
    path('izdatelstvo/<int:pk>', views.IzdatelstvoView.as_view(), name="view-izdatelstvo"),
    path('izdatelstvo-list/',views.IzdatelstvoListView.as_view(), name="list-izdatelstvo"),
    path('izdatelstvo-add/', views.IzdatelstvoAddView.as_view(), name="add-izdatelstvo"),
    path('izdatelstvo-update/<int:pk>', views.IzdatelstvoUpdateView.as_view(), name="update-izdatelstvo"),
    path('izdatelstvo-delete/<int:pk>', views.IzdatelstvoDeleteView.as_view(), name="delete-izdatelstvo"),
    path('zhanr/<int:pk>', views.ZhanrView.as_view(), name="view-zhanr"),
    path('zhanr-list/',views.ZhanrListView.as_view(), name="list-zhanr"),
    path('zhanr-add/', views.ZhanrAddView.as_view(), name="add-zhanr"),
    path('zhanr-update/<int:pk>', views.ZhanrUpdateView.as_view(), name="update-zhanr"),
    path('zhanr-delete/<int:pk>', views.ZhanrDeleteView.as_view(), name="delete-zhanr"),
    path('series/<int:pk>', views.SeriesView.as_view(), name="view-series"),
    path('series-list/',views.SeriesListView.as_view(), name="list-series"),
    path('series-add/', views.SeriesAddView.as_view(), name="add-series"),
    path('series-update/<int:pk>', views.SeriesUpdateView.as_view(), name="update-series"),
    path('series-delete/<int:pk>', views.SeriesDeleteView.as_view(), name="delete-series"),

]