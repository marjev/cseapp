from django.views.generic import DetailView, ListView

from .models import Task


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskDetail(DetailView):
    queryset = Task.objects.all()
    template_name = 'task_detail.html'
