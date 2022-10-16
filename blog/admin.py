from django.contrib import admin
from .models import Author, Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Autopopulates slug

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(language=request.LANGUAGE_CODE)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def get_queryset(self, request):
        categories = Category.objects.filter(language=request.LANGUAGE_CODE)
        qs = super().get_queryset(request)
        return qs.filter(categories__in=categories)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
