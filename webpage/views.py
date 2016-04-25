from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
	title = "Hello there"
	
	#if request.method == "POST":
		#print (request.POST)
	print (request)

	form = SignUpForm(request.POST or None) #if post data send through form or none
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "NA"
		instance.save() #saves data
		print (instance.email)
	
	instance = form.save(commit=False)
	print (instance.full_name)
	
	context = {
		"template_title": title,
		"form": form,
	}
	return render(request, "home.html", context)
