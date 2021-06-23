from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('delete/<int:taskid>/', views.delete, name='delete'),
    # path('update/<int:taskid>/', views.update, name='update'),
    path('cbvcreate/', views.TaskCreateView.as_view(), name='cbvcreate'),
    path('cbvlist/', views.TaskListView.as_view(), name='cbvlist'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]