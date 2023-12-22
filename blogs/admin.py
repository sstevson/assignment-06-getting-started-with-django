from django.contrib import admin

from blogs.models import Post, Category


class PostInline(admin.StackedInline):
    model = Post
    foreign_key = 'Category'


class CategoryInline(admin.TabularInline):
    model = Category
    foreign_key = 'Posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    inlines = [
        CategoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    exclude = ('posts',)
