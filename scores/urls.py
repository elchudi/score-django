from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import JsonResponse


def process_ranking(request):
    print request.GET.get('clase')
    print request.GET.get('alumno')
    print request.GET.get('ranking')
    return JsonResponse({'message':'ok'})

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scores.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^ranking/$', process_ranking),
)
