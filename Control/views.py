from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from Contact.models import Testimony, PrayerRequest
from Control.models import Program
from .forms import ProgramForm, BulkEmail, BulkText, ImageForm, VideoForm, AudioForm
from Home.models import UserUpdate
from django.contrib.auth import login, logout, authenticate
from Media.models import Photo_Gallery
from django.core.mail import BadHeaderError, send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from_email = settings.EMAIL_HOST_USER

class Control(LoginRequiredMixin, View):
    login_url = 'signin'
    def get(self, request, *args, **kwargs):
        return render (request, 'Control/control.html')


class Pending_Testimoniy(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request, *args, **kwargs):
        testimony = Testimony.objects.filter(Approved=False).order_by('-created_time')
        return render (request, 'Control/testimony_list.html', {'testimony':testimony})


class Prayers(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request, *args, **kwargs):
        prayer = PrayerRequest.objects.all()
        return render (request, 'Control/prayer_list.html', {'prayer':prayer})


class Programs(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request, *args, **kwargs):
        return render (request, 'Control/add_programs.html',)

    def post (self, request, *args, **kwargs):
        user = UserUpdate.objects.all()
        recipient_list = []
        if request.method == 'POST':
            church = request.POST.get('church')
            presents = request.POST.get('presents')
            theme = request.POST.get('theme')
            date = request.POST.get('date')
            time = request.POST.get('time')
            venue = request.POST.get('venue')
            enquiry = request.POST.get('enquiry')
            ministers = request.POST.get('ministers')
            design = request.FILES.getlist('design')
            Program.objects.create(Church_Name = church, Presents = presents, Theme = theme, Date = date, Time = time, Venue = venue, Enquiry_Lines = enquiry, Ministering = ministers, Program_Design = design,)
            subject = "Announcements (new program update)"
            # message = 'This is ti brint to your notice'
            message = f"{church} \n\n presents: {presents} \n\n Theme: {theme} \n\n Date: {date} \n\n Time: {time} \n\n Venue: {venue} \n\n Ministering{ministers}. \n\n For enquiryies, contact{enquiry}"
            [recipient_list.append(mail) for mail in user]
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Message sent',  extra_tags='success')
                return render (request, 'Control/add_programs.html',)
            except BadHeaderError:
                messages.info(request, 'Invalaid header',  extra_tags='info')
            messages.info(request, 'Message not automatically sent to users. Please send message mannually to update your users',  extra_tags='info')
        return render (request, 'Control/add_programs.html',)



class user_email(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request, *args, **kwargs):
        users = UserUpdate.objects.all()
        context = {'users':users}
        return render (request, 'Control/user_email.html', context)
    
class user_number(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request, *args, **kwargs):
        users = UserUpdate.objects.all()
        context = {'users':users}
        return render (request, 'Control/user_number.html', context)
    

class program_detail(LoginRequiredMixin, View):
    login_url = 'signin'
    
    def get(self, pk, request, *args, **kwargs):
        program = Program.objects.get(id=pk)
        context = {'program':program}
        return render (request, 'Control/program_detail.html', context)

def Signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.info(
            request, 'invalid username or password')
    return render(request, 'Control/login.html')

def Signout(request):
    logout(request)
    return redirect('index')


class bulk_email(LoginRequiredMixin, View):
    login_url = 'signin'

    def get (self, request, *args, **kwargs):
        return render (request, 'Control/bulk_mail_message.html')

    def post (self, request, *args, **kwargs):
        user = UserUpdate.objects.all()
        recipient_list = []
        if request.method == 'POST':
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            [recipient_list.append(mail) for mail in user]
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Message sent',  extra_tags='success')
                return render (request, 'Control/bulk_mail_message.html')
            except BadHeaderError:
                messages.success(request, 'Invalaid header',  extra_tags='info')
            messages.success(request, 'Message not sent',  extra_tags='info')
        return render (request, 'Control/bulk_mail_message.html')

     
class bulk_text(LoginRequiredMixin, View):
    login_url = 'signin'

    def get (self, request, *args, **kwargs):
        form = BulkText()
        return render (request, 'Control/bulk_sms_message.html', {'form':form})

class add_image(LoginRequiredMixin, View):
    login_url = 'signin'

    def get (self, request, *args, **kwargs):
        form = ImageForm()
        return render (request, 'Control/add_image.html', {'form':form})
    
    def post (self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'image added',  extra_tags='success')
                return render (request, 'Control/add_image.html', {'form':form})
            messages.success(request, 'Image not Uploaded',  extra_tags='info')
        return render (request, 'Control/add_image.html', {'form':form})

class add_video(LoginRequiredMixin, View):
    login_url = 'signin'

    def get (self, request, *args, **kwargs):
        form = VideoForm()
        return render (request, 'Control/add_video.html', {'form':form})
    
    def post (self, request, *args, **kwargs):
        if request.method == 'POST':
            form = VideoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'video added', extra_tags='success')
                return render (request, 'Control/add_video.html', {'form':form})
            messages.info(request, 'Sorry, form cannot be uploaded now please try again',  extra_tags='info')
        return render (request, 'Control/add_video.html', {'form':form})

class add_audio(LoginRequiredMixin, View):
    login_url = 'signin'

    def get (self, request, *args, **kwargs):
        form = AudioForm()
        return render (request, 'Control/add_audio.html', {'form':form})

    def post (self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AudioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'audio added', extra_tags='success')
                return render (request, 'Control/add_audio.html', {'form':form})
            messages.info(request, 'Sorry, form cannot be uploaded now please try again',  extra_tags='info')
        return render (request, 'Control/add_audio.html', {'form':form})

        