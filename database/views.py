from django.shortcuts import render, redirect

from .models import Task, Result


def task_list(request):
    form = Task.objects.all()
    print("Tasks", form)
    return render(request, 'index.html', {'form': form})


def result_list(request):
    form = Result.objects.all().order_by('date').reverse()
    form.reverse()
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
