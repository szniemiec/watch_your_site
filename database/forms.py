from django import forms

from database.models import Task


class TaskForm(forms.ModelForm):
    url = forms.CharField(max_length=200)
    interval = forms.IntegerField()

    class Meta:
        model = Task
        fields = ['url', 'interval']


class ResultForm(forms.Form):
    result_id = forms.IntegerField
    http_code = forms.CharField(max_length=50)
    date = forms.DateTimeField
    task_id = forms.IntegerField
