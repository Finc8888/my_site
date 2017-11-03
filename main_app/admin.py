from django.contrib import admin

# Register your models here.
from .models import Work
from .models import Hobby
from .models import Master
admin.site.register(Work)
admin.site.register(Hobby)
admin.site.register(Master)