from django.contrib import admin
from.models import Category, Recipe

# Register your models here.
class CateegoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CateegoryAdmin)