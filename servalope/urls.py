from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from servalope.views import *

app_name = 'servalope'
urlpatterns = [
    url(r'^mailings/$', login_required(MailingListView.as_view()),name="mailing-list"),
    url(r'^mailings/create$', login_required(CreateMailing.as_view()),name="create-mailing"),
    url(r'^mailings/(?P<pk>[0-9])+/$', login_required(MailingDetailView.as_view()),name="mailing"),
    url(r'^accounts/register$',RegisterView.as_view(),name='register'),
    url('^accounts/', include('django.contrib.auth.urls')),
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^', login_required(MailingListView.as_view()),name="index"),
]
