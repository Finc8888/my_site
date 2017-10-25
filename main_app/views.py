from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def main(request):
	return(render_to_response("index.html"))
def study(request):
	return(render_to_response("study.html"))
def work(request):
	return(render_to_response("work.html"))