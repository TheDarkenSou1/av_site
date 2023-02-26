from django.contrib import admin
from .models import Category, Dish, Why_us, Chef, Response, Event, Gallery, About, Footer


class DishTabularInline(admin.TabularInline):
    model = Dish


class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishTabularInline]

    class Meta:
        model = Category


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish)
admin.site.register(Why_us)
admin.site.register(Chef)
admin.site.register(Response)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Footer)
