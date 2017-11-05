from django.core.management.base import BaseCommand, CommandError
from main_app .models import *
from datetime import date

class Command(BaseCommand):
	def handle(selfr, *args, **options):
		organizations = [
		        {'name': 'Google', 'region': 'США', 'tax_id': 123456, 'site': 'https://google.ru/'},
		        {'name': 'Samsung', 'region': 'Корея', 'tax_id': 666122, 'site': 'http://samsung.com/'},
		        {'name': 'Mail.ru', 'region': 'Москва', 'tax_id': 666124, 'site': 'http://www.mail.ru/'},]
		works = [
		    {'name': 'Google', 'post': 'Инженер',
		     'desc': 'Настройка серверов Google'},
		    {'name': 'Samsung', 'post': 'Консультант мобильной разработки',
		     'desc': 'Разработка девайсов мобильных приложений'},
		    {'name': 'Mail.ru', 'post': 'Системный администратор',
		     'desc': 'Администрирование сайта'}]
		hobbies = [
		    {'name': 'Программирование'},
		    {'name': 'Занятия спортом'}]
		studies = [    
		    {
		        'name': 'Донской Государственный Технический Университет',
		        'date_start':date(year=2010, month=1, day=1),
		        'date_end':date(year=2016, month=1, day=1),
		        'facultet': 'Автоматизация технологических процессов и производств'},]
		Organization.objects.all().delete()
		for organization in organizations:
		    organization = Organization(**organization)
		    organization.save()

		Work.objects.all().delete()
		for work in works:
		    org_name = work["name"]
		    # Получаем организацию по имени
		    organization = Organization.objects.get(name=org_name)
		    # Заменяем название организации объектом
		    work['name'] = organization
		    work = Work(**work)
		    work.save()

		Hobby.objects.all().delete()
		for hobby in hobbies:
		    hobby = Hobby(**hobby)
		    hobby.save()

		Study.objects.all().delete()
		for study in studies:
			study = Study(**study)
			study.save()
