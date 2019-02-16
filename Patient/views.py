from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from .forms import PatientForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from . import ML
import datetime



class profile(View):
    form_class = PatientForm
    template_name = 'profile.html'
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form =self.form_class(request.POST)

        if form.is_valid():
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            bmi = form.cleaned_data['bmi']
            no_of_children = form.cleaned_data['no_of_children']
            regular_smoker = form.cleaned_data['regular_smoker']
            data =[]
            print(sex)
            print(regular_smoker)
            if sex=='male':
                sex=0
            else:
                sex=1
            if regular_smoker=='yes':
                regular_smoker=1
            else:
                regular_smoker=0
            data.extend([age, sex, bmi, no_of_children, regular_smoker])
            data1 = [data]
            print(data1)
            y=ML.training(data1)
            print(y)


            return render(request, 'result.html', {'y':y[0]})
