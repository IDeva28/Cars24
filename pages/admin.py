from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

	def thumbnail(self,object):
		return format_html('<img src="{}" width="40" />'.format(object.photo.url))

	thumbnail.short_description = 'Photo'

	list_display = ('id','thumbnail', 'First_Name', 'Last_Name', 'Designation')
	list_display_links = ('id', 'First_Name','thumbnail',)
	search_fields = ('First_Name','Last_Name', 'Designation',)
	list_filter = ('Designation',)

admin.site.register(Team, TeamAdmin)