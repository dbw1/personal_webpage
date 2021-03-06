from django import forms

from .models import SignUp



class ContactForm(forms.Form):
	full_name = forms.CharField(max_length=120,required=False)
	email = forms.EmailField()
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_message=("A Valid Phone number must be entered"))
	message = forms.CharField(widget=forms.Textarea)

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'full_name']

	#example validation method for admin entry forms
	def clean_email(self):
		email = self.cleaned_data.get('email') #prints on server cleaned email address entered in admin 
		# email_base, provider = email.split("@")
		# domain, extension = provider.split(".")
		# if not extension == "edu":
		# 	raise forms.ValidationError("Please use a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		# write validation code here if needed
		return full_name
