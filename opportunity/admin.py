from django.contrib import admin

from .models import Client, Opportunity, Resource, Skill


class NameCommonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('client', )
    list_filter = ('client', )
    search_fields = ('client__name', )


admin.site.register(Client, NameCommonAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Resource, NameCommonAdmin)
admin.site.register(Skill, NameCommonAdmin)
