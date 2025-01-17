from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.object_list  # Pass the object_list to the context
        return context


class ProjectEditView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_edit.html'
    success_url = reverse_lazy('projects:index')  # Use reverse_lazy for dynamic URL resolution


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:index')   


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:project_list')
