from django.shortcuts import render

from .models import Job

def home(request):
    # fetch all job objects from database
    jobs = Job.objects
    # classic list of jobs
    return render(request, 'jobs/home.html', {'jobs' : jobs})