from django import forms
from todo.models import Task

class TaskForm(forms.ModelForm):
    td_description = forms.CharField(
        widget=forms.Textarea(),
        required=False
    )
    class Meta:
        model = Task
        fields = (
            'td',
            'td_description',
            'deadline',
            'status',
        )