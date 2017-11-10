from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def bonus(request):
	return render_to_response("contact.html")
