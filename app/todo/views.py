from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from todo.forms import TaskForm
from todo.models import Task


class IndexView(generic.TemplateView):
    template_name = 'todo/index.html'


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    queryset = Task.objects.all()
    template_name = 'todo/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')


class TaskListView(LoginRequiredMixin, generic.ListView):
    queryset = Task.objects.all()
    template_name = 'task_list.html'