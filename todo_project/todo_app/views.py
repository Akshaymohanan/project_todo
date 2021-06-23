from django.contrib import messages
from . forms import Todoforms
from django.shortcuts import render, redirect
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
        messages.success(request, "New Task Created")
        return redirect('/')

    return render(request, 'task.html', {'obj1': obj1})


class TaskCreateView(CreateView):
    model = Task
    template_name = 'add.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    success_url = reverse_lazy('cbvlist')


class TaskListView(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'obj1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlist')


# def home(request):
#     obj1 = Task.objects.all()
#     if request.method=='POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         date = request.POST.get('date')
#         obj = Task(name=name, priority=priority, date=date)
#         obj.save()
#         messages.success(request, "New Task Created")
#
#     return render(request, 'home.html', {'obj1': obj1})
#
#
# def delete(request,taskid):
#     task=Task.objects.get(id=taskid)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('/')
#     return render(request, 'task_delete.html', {'task': task})
#
#
# def update(request,taskid):
#     task = Task.objects.get(id=taskid)
#     form = Todoforms(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'task_edit.html', {'task': task, 'form': form})
