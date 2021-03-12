from django.shortcuts import render

from .models import Site


def site_info(request):
    form = Site.objects.all()
    print("Sites", form)
    return render(request, 'siteslist.html', {'form': form})
