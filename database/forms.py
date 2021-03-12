from django import forms


class SiteForm(forms.Form):
    site_id = forms.IntegerField()
    site_url = forms.CharField(max_length=200)
    check_interval = forms.IntegerField()
