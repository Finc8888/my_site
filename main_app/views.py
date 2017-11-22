from django.shortcuts import render
from django.shortcuts import render_to_response
import datetime

from .models import Organization
from .models import Work
from .models import Hobby
from .models import Master
from .models import Study
from django.shortcuts import get_object_or_404
# from .models import Logo

# Create your views here.
def main(request):
	# hobby = ['программирование','радиодело', 'занятия спортом']
	hobby = Hobby.objects.all()
	# cur_hobby = Hobby.objects.filter
	print("------>hobby:",hobby)
	# print("------>cur_hobby:",cur_hobby)
	master = Master.objects.all()
	age = master[0].age
	name = master[0].name
	second_name = master[0].second_name
	# img = Hobby.objects.all()
	logo = Hobby.objects.exclude(image = "logo1/coding.jpg" )
	# print("------>logo:",logo)
	wrap = list(zip(hobby, logo))
	return render_to_response('index.html', {'hobby': hobby,'age':age,'name':name, 
		'second_name':second_name, 'wrap':wrap })
def study(request):
	my_study = Study.objects.all()
	print(my_study)
	where = my_study[0].name
	when = my_study[0].date_end
	what = my_study[0].facultet
	return render_to_response('study.html', {my_study:'my_study','where': where,'when':when,'what':what })
def work(request):
	# place_work = ['Google','Samsung', 'Mail.ru', 'Яндекс']
	place_work = Organization.objects.all()
	return render_to_response('work.html', {'place_work': place_work})
def bonus(request):
	value = datetime.datetime.now()
	return render_to_response("bonus.html", {'value': value})
def work_detail(request, pk):
    work = get_object_or_404(Post, pk=pk)
    return render(request, 'about_me/work_detail.html', {'work': work})