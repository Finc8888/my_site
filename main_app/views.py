from django.shortcuts import render
from django.shortcuts import render_to_response
import datetime

from .models import Work
from .models import Hobby
from .models import Master
# Create your views here.
def main(request):
	# hobby = ['программирование','радиодело', 'занятия спортом']
	hobby = Hobby.objects.all()
	master = Master.objects.all()
	age = master[0].age
	name = master[0].name
	second_name = master[0].second_name
	return render_to_response('index.html', {'hobby': hobby,'age':age,'name':name, 
		'second_name':second_name, })
def study(request):
	return render_to_response("study.html")
def work(request):
	# place_work = ['Google','Samsung', 'Mail.ru', 'Яндекс']
	place_work = Work.objects.all()
	return render_to_response('work.html', {'place_work': place_work})
def bonus(request):
	value = datetime.datetime.now()
	return render_to_response("bonus.html", {'value': value})