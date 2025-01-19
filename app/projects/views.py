from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView, 
    DetailView
)
from django.urls import reverse_lazy
from .models import Project, Area, Goal
from .forms import ProjectForm, ProjectGoalForm


class AreaListView(ListView):
    model = Area
    template_name = 'projects/strategy_list.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    

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


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:index')   


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:project_list')

def assign_goal(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectGoalForm(request.POST)
        if form.is_valid():
            project_goal = form.save(commit=False)
            project_goal.project = project
            project_goal.save()
            return redirect('projects:project_detail', pk=project.id)
    else:
        form = ProjectGoalForm()
    return render(request, 'projects/assign_goal.html', {'form': form, 'project': project})
