from django.shortcuts import render

from .models import Task, Result


def task_list(request):
    form = Task.objects.all()
    print("Tasks", form)
    return render(request, 'index.html', {'form': form})


def result_list(request):
    form = Result.objects.all()
    print("Results", form)
    return render(request, 'results.html', {'form': form})
