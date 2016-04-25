from django.shortcuts import render

# Create your views here.
def home(request):
	title = "Hello there %s" %(request.user)
	context = {
		"template_title": title
	}
	return render(request, "home.html", context)
