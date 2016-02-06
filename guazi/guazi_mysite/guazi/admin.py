from django.contrib import admin
from guazi.models import GuaziCar
# Register your models here.
class GuaziAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'time', 'mile', 'price')
	search_fields = ['name', 'city', 'time', 'mile', 'price']

admin.site.register(GuaziCar, GuaziAdmin)
