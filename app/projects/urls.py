from django.urls import path
from . import views

app_name = 'projects'  # Define the app namespace

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('strategy/', views.AreaListView.as_view(), name='strategy_list'),
    path('index/', views.ProjectListView.as_view(), name='index'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/edit/', views.ProjectEditView.as_view(), name='project_edit'),
    path('<int:pk>/confirm_delete/', views.ProjectDeleteView.as_view(), name='project_confirm_delete'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/assign-goal/', views.assign_goal, name='assign_goal'),
]
