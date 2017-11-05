from django.contrib import admin

# Register your models here.
from .models import Organization
from .models import Work
from .models import Hobby
from .models import Master
from .models import Study
admin.site.register(Organization)
admin.site.register(Work)
admin.site.register(Hobby)
admin.site.register(Master)
admin.site.register(Study)
