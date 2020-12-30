from django.contrib import admin
from .models import car
from django.utils.html import format_html

# Register your models here.

class carAdmin(admin.ModelAdmin):

	def thumbnail(self,object):
		return format_html('<img src="{}" width="40" />'.format(object.car_photo.url))

	thumbnail.short_description = 'car image'

	list_display = ('id','car_title','thumbnail', 'city', 'color', 'model','engine','body_style','fuel_type','isfeatured',)
	list_display_links = ('id','car_title','thumbnail',)
	list_editable = ('isfeatured',)
	search_fields = ('id','car_title','city','model','fuel_type','color',)
	list_filter = ('body_style','model','fuel_type','color','city',)


admin.site.register(car, carAdmin)
