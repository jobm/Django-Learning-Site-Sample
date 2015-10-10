from django.http import HttpResponse
from django.shortcuts import render


from .models import Course
# Create your views here.
def coure_list(request):
    courses = Course.objects.all()
    output = ','.join(courses)
    return HttpResponse(output)
