from django.contrib import admin
from .models import MyBlogs, Author, Comment, Interiors, Exteriors, InteriorImage, ExteriorImage

admin.site.register(MyBlogs)

admin.site.register(Author)

admin.site.register(Comment)

class InteriorImageInline(admin.TabularInline):
    model = InteriorImage
    extra = 3  # Количество дополнительных форм для загрузки изображений

class InteriorsAdmin(admin.ModelAdmin):
    inlines = [InteriorImageInline]

admin.site.register(Interiors, InteriorsAdmin)

class ExteriorImageInline(admin.TabularInline):
    model = ExteriorImage
    extra = 3  # Количество дополнительных форм для загрузки изображений

class ExteriorsAdmin(admin.ModelAdmin):
    inlines = [ExteriorImageInline]

admin.site.register(Exteriors, ExteriorsAdmin)
