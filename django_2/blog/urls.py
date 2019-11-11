from django.urls import path, re_path
from .views import post_list, post_detail

app_name='blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
            post_detail,
            name='post_detail')
]