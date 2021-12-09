from django.urls import path
from first_app import views


urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name="post_detail")

]
