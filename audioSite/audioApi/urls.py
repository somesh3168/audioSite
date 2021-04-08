from django.urls import path
from . import views
# from .views import CreateAPI, DeleteAPI, UpdateAPI, audiofiletype
urlpatterns = [
    
    path('get/<audioFileType>/<int:audioFileID>/', views.listAPI.as_view(), name = 'get_api'),
    path('get/<audioFileType>/', views.listAPI.as_view(), name = 'get_api'),
    path('create/<audioFileType>/', views.listAPI.as_view(), name = 'post_api'),
    path('update/<audioFileType>/', views.DelUpdateAPI.as_view(), name = 'put_api'),
    path('update/<audioFileType>/<int:audioFileID>/', views.DelUpdateAPI.as_view(), name = 'put_api'),
    path("del/<audioFileType>/<int:audioFileID>/",views.DelUpdateAPI.as_view(),name="delete_api"),
    path("del/<audioFileType>/",views.DelUpdateAPI.as_view(),name="delete_api"),
    path('', views.home, name = 'home'),
]
