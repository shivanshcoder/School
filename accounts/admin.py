from django.contrib import admin
from .models import Parent, Student, Teacher, AuthUser, SchoolClass, ReferalSource



admin.site.register(ReferalSource)
admin.site.register(SchoolClass)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Teacher)
# # # Register your models here.
# admin.site.register(Parent, UserAdmin)
# admin.site.register(Teacher, UserAdmin)
# admin.site.register(Student, UserAdmin)
# admin.site.register(AuthUser)
# admin.site.register(BaseUser, StudentAdmin)
