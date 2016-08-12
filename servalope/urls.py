from django.conf.urls import url

from servalope.views import *

app_name = 'servalope'
urlpatterns = [
    url(r'^mailings/$', MailingListView.as_view(),name="mailing-list"),
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
