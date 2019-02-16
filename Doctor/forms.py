from django import forms

class DiabeticForm(forms.Form):
    pregnancies = forms.IntegerField()
    glucose = forms.IntegerField()
    bloodpressure = forms.IntegerField()
    skinthickness = forms.IntegerField()
    insulin = forms.IntegerField()
    bmi = forms.FloatField()
    diabetespedigreefunction = forms.FloatField()
    age = forms.IntegerField()
