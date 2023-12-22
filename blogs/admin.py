from django.contrib import admin

from blogs.models import Post, Category


class PostInline(admin.StackedInline):
    model = Post
    foreign_key = 'category'


class CategoryInline(admin.TabularInline):
    model = Category
    foreign_key = 'post'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('posts',)
