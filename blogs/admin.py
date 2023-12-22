from django.contrib import admin

from blogs.models import Post, Category


class PostInline(admin.TabularInline):
    model = Post


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('posts',)
