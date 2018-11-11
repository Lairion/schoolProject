from django.contrib import admin
from learning.admin import MarkInline
from .models import Pupil,SchoolClass
# Register your models here.

class PupilAdmin(admin.ModelAdmin):
    '''
        Admin View for Puple
    '''
    list_display = ('first_name','last_name','birthday','in_class')
    list_filter = ('first_name','last_name','birthday','in_class')
    inlines = [
        MarkInline,
    ]
    search_fields = ('first_name','last_name','birthday','in_class')

admin.site.register(Pupil, PupilAdmin)

class PupilInline(admin.TabularInline):
    model = Pupil

class SchoolClassAdmin(admin.ModelAdmin):
    '''
        Admin View for SchoolClass
    '''
    list_filter = ('number','alfa')
    inlines = [
        PupilInline,
    ]
    search_fields = ('number','alfa')

admin.site.register(SchoolClass, SchoolClassAdmin)