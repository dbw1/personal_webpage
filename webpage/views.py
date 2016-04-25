from django.shortcuts import render

from .forms import SignUpForm

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
		if not instance.full_name:
			instance.full_name = "NA"
		instance.save() #saves data
		context = {
		"title": "Thank you",
		}	
	
	return render(request, "home.html", context)
