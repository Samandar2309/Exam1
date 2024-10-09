from django.contrib import admin
from .models import About, FAQ, Our_Clients, Comments, Posts, ServiceCategories, Services, OurService, Contact, Pricing, PriceList, Teachers, Coworkers

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Our_Clients)
class OurClientsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')
    search_fields = ('name', 'profession')

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ServiceCategories)
class ServiceCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('price',)
    search_fields = ('price',)

@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Coworkers)
class CoworkersAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

