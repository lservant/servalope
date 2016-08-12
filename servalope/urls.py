from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from servalope.views import *

app_name = 'servalope'
urlpatterns = [
    # url(r'^', login_required(MailingListView.as_view()),name="index"),
    url(r'^mailings/$', login_required(MailingListView.as_view()),name="mailing-list"),
    url('^accounts/', include('django.contrib.auth.urls')),
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
