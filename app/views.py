from django.shortcuts import render
import datetime
# Create your views here.

def filters(request):
    dz=datetime.datetime.now()
    d={'a':'men WILL be MEN ALways','dz':dz,'c':1}
    return render(request,'filter.html',d)