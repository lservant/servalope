from django.shortcuts import render
from django.views.generic import *
from servalope.models import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



# Create your views here.
class MailingListView(ListView):
    """Displays a list of mailings for a given user"""

    model = Mailing

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MailingListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['mailing_list'] = Mailing.objects.all()

        return context
