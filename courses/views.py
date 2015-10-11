from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render


from .models import Course
# Create your views here.
def coure_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', { 'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course,pk=pk)
    return render(request,'courses/course_detail.html',{'course':course})

def step_detail(request,course_pk, step_pk):
    course = get_object_or_404(Step,course_id = course_pk,pk = step_pk)
    return render(request,'courses/step_detail.html',{'step': step})
