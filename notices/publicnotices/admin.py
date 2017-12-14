from django.contrib import admin

from .models import PublicNotice, Advertiser, Medium, Entry


class PublicNoticeAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'posted_by', 'date_posted']


class PublicNoticeInstanceAdmin(admin.ModelAdmin):
	list_display = ['id', 'when_published', 'where_published']


class AdvertiserAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'company', 'designation']





admin.site.register(PublicNotice, PublicNoticeAdmin)
# admin.site.register(PublicNoticeInstance, PublicNoticeInstanceAdmin)
admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Medium)
admin.site.register(Entry)