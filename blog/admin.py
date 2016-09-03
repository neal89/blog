from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	fields = ('author', 'title', 'category', 'text', 'cover_image', 'created_date', 'published_date', 'published','slug')
	list_filter = ['published_date', 'published']
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
