from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from servalope.models import *
from django.contrib.auth import logout, views as auth_views
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

from servalope.forms import *

# Create your views here.
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        clean = form.cleaned_data
        u = clean['username']
        p = clean['password']
        e = clean['email']
        user = User.objects.create_user(u,e,p)
        user.first_name = clean['first_name']
        user.last_name = clean['last_name']
        user.save()

        return super(RegisterView, self).form_valid(form)

class CreateMailing(FormView):
    form_class = MailingForm
    success_url = '/mailings/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        clean = form.cleaned_data
        n = clean['name']
        d = clean['date']
        m = clean['message']
        c = self.request.user
        mailing = Mailing(name=n,date=d,message=m,customer=c)
        mailing.save()

        return super(CreateMailing, self).form_valid(form)

class MailingListView(ListView):
    """Displays a list of mailings for a given user"""

    model = Mailing

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MailingListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_staff or user.is_superuser:
            print('Show all Mailings')
            context['mailing_list'] = Mailing.objects.all()
        else:
            context['mailing_list'] = Mailing.objects.filter(customer=user)

        context['create_form'] = MailingForm()

        return context

class MailingDetailView(DetailView):
    """Displays the guests and RSVP status for a given mailing"""

    model = Mailing

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MailingDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['guest_list'] = Guest.objects.filter(mailing=context['mailing'])

        return context
