from django.shortcuts import render
from django.shortcuts import render_to_response
import datetime
# Create your views here.
def main(request):
	hobby = ['программирование','радиодело', 'занятия спортом']
	age = datetime.date(1988,3,8)
	name = 'владимир'
	second_name = 'Приходько'
	return render_to_response('index.html', {'hobby': hobby,'age':age,'name':name, 
		'second_name':second_name, })
def study(request):
	return render_to_response("study.html")
def work(request):
	place_work = ['Google','Samsung', 'Mail.ru', 'Яндекс']
	return render_to_response('work.html', {'place_work': place_work})
def bonus(request):
	value = datetime.datetime.now()
	return render_to_response("bonus.html", {'value': value})