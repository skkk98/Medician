from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, View
from .forms import DiabeticForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from . import DiabetesRegression
from Home.models import Detailuser
import datetime



class docprofile(View):
    form_class = DiabeticForm
    template_name = 'docpro.html'
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form =self.form_class(request.POST)

        if form.is_valid():
            pregnancies = form.cleaned_data['pregnancies']
            glucose = form.cleaned_data['glucose']
            bloodpressure = form.cleaned_data['bloodpressure']
            skinthickness = form.cleaned_data['skinthickness']
            insulin = form.cleaned_data['insulin']
            bmi = form.cleaned_data['bmi']
            diabetespedigreefunction = form.cleaned_data['diabetespedigreefunction']
            age = form.cleaned_data['diabetespedigreefunction']
            data = []
            data.extend([pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age])
            data1 = [data]
            user_id = request.user
            print(user_id)
            element = Detailuser.objects.get(user=user_id)
            print(element.Specialization)
            if element.Specialization == 'Endocrinologist':
                y,score = DiabetesRegression.training(data1)
                print(y)
                return render(request, 'resultdiabetic.html', {'y':y, 'score':score})

            return HttpResponse("successfull")
