from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
	title = "Hello there"
	
	form = SignUpForm(request.POST or None) #if post data send through form or none
	context = {
		"title": title,
		"form": form,
	}
	#if request.method == "POST":
		#print (request.POST)
		
	if form.is_valid():
		
		instance = form.save(commit=False)

		# validation option 1
		if not instance.full_name:
			instance.full_name = "NA"
		
		# validation option 2
		# full_name = form.cleaned_data.get("full_name")
		# if not full_name:
		# 	full_name = "NA"
		# instance.full_name = full_name



		instance.save() #saves data
		context = {
		"title": "Thank you",
		}	
	
	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		full_name = form.cleaned_data.get("full_name")
		form_email = form.cleaned_data.get("email")
		phone = form.cleaned_data.get("phone")
		message = form.cleaned_data.get("message")
		subject = 'Site Contact Form'
		email_from_add = settings.EMAIL_HOST_USER
		recipient_list = [email_from_add]
		contact_message = """
		Name: %s
		Phone Number: %s
		Email: %s
		Message: %s
		""" % (full_name, phone, form_email, message)
		send_mail(subject,
				contact_message,
				email_from_add,
				recipient_list,
				fail_silently=True)

		# for key in form.cleaned_data:
		# 	print (key, form.cleaned_data.get(key)) #get(key) returns key value
	context = {
		"form" : form
	}
	return render(request, "forms.html", context)
