from django.shortcuts import render, get_object_or_404, redirect, reverse, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'userdetails/login.html'

    # displaying a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # processing the form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)

            # cleaned (normalized) data
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            # user.set_password(pw)

            # returns user objects if credentials are correct
            user = authenticate(username=un, password=pw)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    user_profile = UserProfile.objects.get(user=user)
                    rfid_list = UserRfid.objects.filter(user=user)
                    available_rfids = []
                    for rfid in rfid_list:
                        r = RfidCar.objects.get(rfid_no=str(rfid))
                        available_rfids.append(r)
                    context = {'user':user, 'user_profile':user_profile,'available_rfids':available_rfids}
                    return render(request,'userdetails/dashboard.html',context)
        return render(request, self.template_name, {'form' : form})

def logout(request):
    logout(request)
    form = UserForm(None)
    return render(request, 'userdetails/login.html', {'form': form})


def journey(request, pk):
    r = RfidCar.objects.get(pk=pk)
    return render(request, 'userdetails/journey.html', {'r':r})


def payment(request, pk):
    r = RfidCar.objects.get(pk=pk)
    return render(request, 'userdetails/payment.html', {'r': r})