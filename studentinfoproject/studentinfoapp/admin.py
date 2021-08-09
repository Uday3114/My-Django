from django.contrib import admin
from .models import Student_Info, Movies


# Register your models here.
class Student_InfoAdmin(admin.ModelAdmin):
    '''
        Admin View for Student_Info
    '''
    list_display = ('FIRSTNAME','LASTNAME','CLGNAME','BRANCH','DOB','GENDER','DEPT','STUDENT_ID')
admin.site.register(Student_Info, Student_InfoAdmin)


class MovieAdmin(admin.ModelAdmin):
    '''
        Admin View for Student_Info
    '''
    list_display = ('Name','Actor','Actress','Budget')


admin.site.register(Movies, MovieAdmin)
