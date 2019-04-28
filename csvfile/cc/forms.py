from django  import forms

class contactform(forms.Form):
    rollno = forms.IntegerField();
    name= forms.CharField();
    category = forms.ChoiceField(choices=[('question','question'),('other','other')])




