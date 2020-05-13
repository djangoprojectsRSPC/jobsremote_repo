from django.shortcuts import render
from testapp.models import * # or HydJobs,BloreJobs,PuneJobs,ChennaiJobs

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs(request):
    jobs_list = HydJobs.objects.order_by('date')
    my_dict = {'Hjobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def blorejobs(request):
    jobs_list = BloreJobs.objects.order_by('company')
    my_dict = {'Bjobs_list':jobs_list}
    return render(request,'testapp/blorejobs.html',context=my_dict)

def punejobs(request):
    jobs_list = PuneJobs.objects.order_by('title')
    my_dict = {'Pjobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)

def chennaijobs(request):
    jobs_list = ChennaiJobs.objects.order_by('email')
    my_dict = {'Cjobs_list':jobs_list}
    return render(request,'testapp/chennaijobs.html',context=my_dict)
