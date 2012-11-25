from critmixes.models import Critmix
from critmixes.models import Crit
from django.contrib import admin

#admin.site.register(Critmix)
#admin.site.register(Crit)

class CritInline(admin.TabularInline):
    model = Crit
    extra = 3

class CritmixAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['mix_url']}),
        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CritInline]

admin.site.register(Critmix, CritmixAdmin)
