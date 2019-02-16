from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Detailuser
from .forms import RegisterForm, LoginForm

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

class Register(View):
    form_class = RegisterForm
    template_name = 'Register.html'
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            Type = form.cleaned_data['Type']
            name = form.cleaned_data['name']
            specialization = form.cleaned_data['specialization']
            if password == confirm_password:
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                login(request, user)
                user_id = request.user
                if Type is 'DOCTOR':
                    reg = Detailuser(user=user_id, Name=name, Type=Type, Specialization=specialization)
                    reg.save()
                else:
                    reg = Detailuser(user=user_id, Name=name, Type=Type)
                    reg.save()
                #regevent = Regevent(user=user_id)
                #regevent.save()
                logout(request)
                return HttpResponse('successfully registered <a href="/login"><strong>Click Here</strong></a><a>to Login</a>')
            else:
                return HttpResponse('Passwords do not match <a href=""><strong>Click Here</strong></a><a>to try again</a>')

        return render(request, self.template_name, {'form': form})

class Login(View):
    form_class = LoginForm
    template_name = 'Login.html'
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form =self.form_class(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            Type = form.cleaned_data['Type']
            specialization = form.cleaned_data['specialization']
            print(specialization)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user_id = request.user
                find_details = Detailuser.objects.get(user=user_id)
                name = find_details.Name
                #if Detailuser.objects.filter(user=request.user, Name=name, Type=Type, Specialization=specialization).exists():
                return HttpResponseRedirect('/'+Type.lower()+'/profile') #check specialization to show profile corresponding ML model
            else:
                return HttpResponse('<a href=""><strong>Click Here</strong></a> <a>to try again!</a>')
        else:
            return HttpResponse('<a href=""><strong>Click Here</strong></a> <a>Form is not valid!</a>')
        return render(request, self.template_name, {'form': form})
