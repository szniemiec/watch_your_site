from django import forms


class TaskForm(forms.Form):
    site_id = forms.IntegerField()
    site_url = forms.CharField(max_length=200)
    check_interval = forms.IntegerField()


class ResultForm(forms.Form):
    result_id = forms.IntegerField
    http_code = forms.CharField(max_length=50)
    date = forms.DateTimeField
    task_id = forms.IntegerField
