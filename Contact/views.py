from django.shortcuts import render, redirect
from django.views import View
from .forms import PrayerRequestForm, TestimonyForm
from django.views.generic.edit import FormView
from django.contrib import messages
from .models import Testimony


class Prayer_Request(View):
    def get (self, request, *args, **kwargs):
        form = PrayerRequestForm()
        return render (request, 'Contact/prayer_request.html', {'form':form})

    def post (self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PrayerRequestForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('index')
            messages.info(request, 'Sorry, form cannot be uploaded now please try again',  extra_tags='info')
        return render (request, 'Contact/prayer_request.html', {'form':form})


class Testimony_View(View):
    def get(self, request, *args, **kwargs):
        form = TestimonyForm()
        return render (request, 'Contact/testimony.html', {'form':form})

    def post (self, request, *args, **kwargs):
        if request.method == 'POST':
            form = TestimonyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('index')
            messages.info(request, 'Sorry, form cannot be uploaded now please try again',  extra_tags='info')
        return render (request, 'Contact/testimony.html', {'form':form})

def testimony_accepted(request, pk):
    testimony = Testimony.objects.get(id=pk)
    testimony.Approved = True
    testimony.save()
    return redirect('pending_testimonies')

def testimony_rejected(request, pk):
    testimony = Testimony.objects.get(id=pk)
    testimony.delete()
    return redirect('pending_testimonies')
