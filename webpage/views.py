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
		for key in form.cleaned_data:
			print (key, form.cleaned_data.get(key)) #get(key) returns key value
	context = {
		"form" : form
	}
	return render(request, "forms.html", context)
