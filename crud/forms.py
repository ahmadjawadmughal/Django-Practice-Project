from django import forms
from django.core.validators import RegexValidator
from .models import Person
# class PersonForm(forms.Form):

#     name = forms.CharField(max_length=50)
#     age = forms.IntegerField(min_value=1, max_value=100)
#     country = forms.CharField(max_length=30)
#     phone_no = forms.CharField(max_length= 15, 
#                                validators=[RegexValidator(r"^\+?1?92?\d{9,15}")])
#     email = forms.EmailField(max_length= 30)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "age", "country", "email"]