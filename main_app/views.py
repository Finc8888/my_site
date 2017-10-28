from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def main(request):
	age = 1988
	name = 'Владимир'
	second_name = 'Приходько'
	return render_to_response('index.html', {'age':age,'name':name, 'second_name':second_name})
def study(request):
	return render_to_response("study.html")
def work(request):
	place_work = ['Google','Samsung', 'Mail.ru', 'ООО "Вэб студия"']
	return render_to_response('work.html', {'place_work': place_work})
def bonus(request):
	return render_to_response("bonus.html")