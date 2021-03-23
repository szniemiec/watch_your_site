from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task, Result


def task_list(request):
    form = Task.objects.all()
    print("Tasks", form)
    return render(request, 'index.html', {'form': form})


def result_list(request):
    form = Result.objects.all().order_by('date').reverse()
    print("Results", form)
    return render(request, 'results.html', {'form': form})


def create_task(request):
    if request.method == 'POST':
        if request.POST.get('url') and request.POST.get('interval'):
            task = Task()
            task.url = request.POST.get('url')
            task.interval = request.POST.get('interval')
            task.save()
            return render(request, 'tasks.html')
    else:
        return render(request, 'tasks.html')


def delete_task(request, task_id):
    if request.method == 'POST':
        Task.objects.get(pk=task_id).delete()
    return redirect('/index/')


def update_task(request, task_id):
    context = {}
    obj = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/updatetask/" + task_id)
    context["form"] = form
    return render(request, "updatetask.html", context)
