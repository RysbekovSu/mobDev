from django.contrib import admin

from .models import Teacher, Category, Liked, Article, Words

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(Liked)
admin.site.register(Article)
admin.site.register(Words)


