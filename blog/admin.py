from django.contrib import admin
from .models import Author, Category, Post
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"  # Shows markdown editor
    prepopulated_fields = {"slug": ("title",)}  # Autopopulates slug


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
