from django.contrib import admin
from .models import Faculty,LearnTable,Mark, Pip
from schoolclasses.models import Pupil
from django import forms
# Register your models here.

class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = ['who_get_mark']

    def __init__(self, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)
        try:
            # print("\n".join(dir(self.instance)))
            self.fields['who_get_mark'].queryset = Pupil.objects.filter(
                                        in_class=self.instance.learn_table.for_class)
        except:
            print("New instance")
class PipInline(admin.TabularInline):
    model = Pip
class MarkAdmin(admin.ModelAdmin):
    '''
        Admin View for Mark
    '''
    list_display = ('learn_table','who_get_mark','mark_date',)
    list_filter = ('learn_table','who_get_mark','mark_date',)
    search_fields = ('learn_table','who_get_mark','mark_date',)
    fields = ('learn_table','who_get_mark','mark_date',)

    inlines = [
        PipInline,
    ]
    form = MarkForm
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "who_get_mark":
    #         print("\n".join(dir(request)))
    #         print("\n".join(kwargs.keys()))
    #         # kwargs["queryset"] = Pupil.objects.filter(in_class = request.)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Mark, MarkAdmin)

class MarkInline(admin.StackedInline):
    model = Mark
    

class LearnTableAdmin(admin.ModelAdmin):
    '''
        Admin View for LearnTable
    '''
    list_display = ('faculty','for_class',)
    list_filter = ('faculty','for_class',)
    
    search_fields = ('faculty','for_class',)
    

admin.site.register(LearnTable, LearnTableAdmin)

class LearnTableInline(admin.TabularInline):
    model = LearnTable


class FacultyAdmin(admin.ModelAdmin):
    '''
        Admin View for Faculty
    '''
    list_display = ('name',)
    list_filter = ('name',)
    inlines = [
        LearnTableInline,
    ]
    search_fields = ('name',)

admin.site.register(Faculty, FacultyAdmin)