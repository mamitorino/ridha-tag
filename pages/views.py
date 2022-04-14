import imp
from django.shortcuts import render
from .formes import FormLogen
from .models import Show
# Create your views here.


def index (request):

    if request.method == 'POST':
        data = FormLogen(request.POST)
        if data.is_valid:
            data.save()
    return render(request , 'pages/index.html',{'lf':FormLogen ,'pro':Show.objects.get()})