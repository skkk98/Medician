from django import forms
#age, sex, bmi, no:of children, Smoker yes or no, Region southwest southeaast northwest northeast
class PatientForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.CharField(widget=forms.Select(choices=(('male','MALE'),('female', 'FEMALE'))))
    bmi = forms.FloatField()
    no_of_children = forms.IntegerField()
    regular_smoker = forms.CharField(widget=forms.Select(choices=(('yes','YES'),('no','NO'))))
    #region = forms.CharField(widget=forms.Select(choices=(('southwest','SOUTHWEST'))))
