from django.forms import ModelForm
from database.models import Site


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ['site_url', 'check_interval']


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()

