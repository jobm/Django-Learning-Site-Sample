from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.coure_list),
    url(r'(?P<pk>\d+)/$',views.course_detail),
]
