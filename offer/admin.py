from django.contrib import admin
from .models import Offer

# Register your models here.
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Offer, OfferAdmin)

