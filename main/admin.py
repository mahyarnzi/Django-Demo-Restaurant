import json
from django.contrib import admin
from main.models import Contact, Newsletter, Addresses, About, Chef, Background, Logo
from django_summernote.admin import SummernoteModelAdmin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ('location',)
    formfield_overrides = {map_fields.AddressField: {'widget':
        map_widgets.GoogleMapsAddressWidget(
            attrs={'data-map-type': 'roadmap',
                   'data - autocomplete - options': json.dumps({'types': ['geocode', 'establishment'],
                                                                'componentRestrictions': {'country': 'ir'}})
                   })
                                                    },
                            }


@admin.register(Chef)
class ChefAdmin(SummernoteModelAdmin):
    list_display = ('name', 'title')
    list_filter = ('title',)
    search_fields = ('name', 'title')
    summernote_fields = ('content',)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'type')
    summernote_fields = ('content',)


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ['title']