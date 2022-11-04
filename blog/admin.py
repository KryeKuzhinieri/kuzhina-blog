from django.contrib import admin
from .models import Author, Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Autopopulates slug


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title", ),
    }

    def get_queryset(self, request):
        qs = self.model.custom_manager.category_by_language
        return qs

    # Removing author field from the admin form.
    # author should be autoadded.
    def get_fields(self, request, obj=None):
        fields = super(PostAdmin, self).get_fields(request, obj)
        fields.remove("author")
        return fields

    def save_model(self, request, obj, form, change):
        # Prepopulates author field.
        if not change:
            obj.author = Author.objects.get(user=request.user)
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
