from django.shortcuts import render

from .models import Task


def task_list(request):
    form = Task.objects.all()
    print("Tasks", form)
    return render(request, 'index.html', {'form': form})
