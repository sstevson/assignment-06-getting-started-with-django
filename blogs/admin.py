from django.contrib import admin

from blogs.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    """displays a menu element to add a category to a post"""

    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
