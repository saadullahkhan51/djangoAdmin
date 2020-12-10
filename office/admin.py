from django.contrib import admin

# Register your models here.
from office.models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Question)
admin.site.register(Choice)
