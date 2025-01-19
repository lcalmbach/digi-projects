from django import forms
from .models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div
from .models import ProjectGoal

class ProjectGoalForm(forms.ModelForm):
    class Meta:
        model = ProjectGoal
        fields = ['goal', 'description']

        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Project Information',
                'title',
                'contact_person',
                # Add other fields here
            ),
            Div(
                Submit('submit', 'Create Project', css_class='btn btn-primary'),
                css_class='text-center'
            )
        )