from django.shortcuts import render, redirect
from django.views import View
from.forms import UserUpdateForm
from django.contrib import messages
from Media.models import Photo_Gallery
from Contact.models import Testimony
from Control.models import Program


class index(View):
    def get(self, request, *args, **kwargs):
        form = UserUpdateForm()
        images = Photo_Gallery.objects.all().order_by('-created_time')[:4]
        testimony = Testimony.objects.filter(Approved=True).order_by('-created_time')[:10]
        program = Program.objects.all().order_by('-created_time')[:5]
        context={
            'program' : program,
            'form': form, 
            'images': images, 
            'testimony': testimony,
        }
        return render(request, 'index.html', context)
    
    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details Submitted')
            return redirect('index')


def About_Omowoli(request):
    return render(request, 'About/about_omowoli.html')

def About_Baba_Aladeolu(request):
    return render(request, 'About/about_baba_aladeolu.html')

def About_Orioke_Aanu(request):
    return render(request, 'About/about_orioke_aanu.html')
