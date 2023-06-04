"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from spravochniki import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author-cbv/<int:pk>', views.AuthorView.as_view()),
    path('author-add-cbv/', views.AuthorAddView.as_view()),
    path('author-update-cbv/<int:pk>', views.AuthorUpdateView.as_view()),
    path('author-delete-cbv/<int:pk>', views.AuthorDeleteView.as_view()),
    path('author-list-cbv/',views.AuthorListView.as_view()),
    path('izdatelstvo-cbv/<int:pk>', views.IzdatelstvoView.as_view()),
    path('izdatelstvo-list-cbv/',views.IzdatelstvoListView.as_view()),
    path('izdatelstvo-add-cbv/', views.IzdatelstvoAddView.as_view()),
    path('izdatelstvo-update-cbv/<int:pk>', views.IzdatelstvoUpdateView.as_view()),
    path('izdatelstvo-delete-cbv/<int:pk>', views.IzdatelstvoDeleteView.as_view()),
    path('zhanr-cbv/<int:pk>', views.ZhanrView.as_view()),
    path('zhanr-list-cbv/',views.ZhanrListView.as_view()),
    path('zhanr-add-cbv/', views.ZhanrAddView.as_view()),
    path('zhanr-update-cbv/<int:pk>', views.ZhanrUpdateView.as_view()),
    path('zhanr-delete-cbv/<int:pk>', views.ZhanrDeleteView.as_view()),
    path('series-cbv/<int:pk>', views.SeriesView.as_view()),
    path('series-list-cbv/',views.SeriesListView.as_view()),
    path('series-add-cbv/', views.SeriesAddView.as_view()),
    path('series-update-cbv/<int:pk>', views.SeriesUpdateView.as_view()),
    path('series-delete-cbv/<int:pk>', views.SeriesDeleteView.as_view()),
    path('', views.HomePage.as_view()),
]
