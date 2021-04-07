from django.contrib import admin
from .models import User, Session, Department, Course, Faculty, Subject, Semester, Student
from django.contrib.auth.admin import UserAdmin
from app.forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.


class UserAdminConfig(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    search_fields = ('email',)
    ordering = ('email',)
    list_display = ('email', 'start_date', 'is_superuser', 'is_staff', 'is_faculty',
                    'is_student', 'is_active')
    list_filter = ('is_active', 'is_faculty',
                   'is_student', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                    'is_faculty', 'is_student', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_faculty', 'is_student', 'is_active')
        }),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
