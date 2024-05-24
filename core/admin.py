from django.contrib import admin
from .models import Swim, Category, Calisthenic, Run, Body

# Register your models here.
admin.site.register(Swim)
admin.site.register(Category)
admin.site.register(Calisthenic)
admin.site.register(Run)
admin.site.register(Body)
