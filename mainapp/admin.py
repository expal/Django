from django.contrib import admin

from mainapp import models
from django.utils.translation import gettext_lazy as _


# Register your models here.


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 10
    list_filter = ["course", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")

    get_course_name.short_description = _("Course")


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preview", "body"]


@admin.register(models.Courses)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CourseTeachers)
class LessonAdmin(admin.ModelAdmin):
    pass
