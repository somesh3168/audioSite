from django.urls import path
from . import views
from .views import CreateAPI, DeleteAPI, UpdateAPI, audiofiletype
urlpatterns = [
    
    path('get/', views.listAPI.as_view(), name = 'get_api'),
    path("create/", views.CreateAPI.as_view(),name="create_api"),
    path("update/<int:pk>/",views.UpdateAPI.as_view(),name="update_api"),
    path("delete/<int:pk>/",views.DeleteAPI.as_view(),name="delete_api"),

    path('home/', views.home, name = 'home'),
]
