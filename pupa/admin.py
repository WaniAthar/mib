from django.contrib import admin
from .models import *

admin.site.site_header = "MIB Admin panel"
admin.site.site_title = "MIB Admin panel"

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','image', 'date']
    ordering = ['title']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(posted_by=request.user)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "posted_by":
            kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class UpdateAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'date']
    ordering = ['title']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(username=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','contact_date']
    ordering = ['name']
    # sort by time
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(contact_date=datetime.datetime.now())

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name','email','image','bio']
    ordering = ['name']

class PupaVolunteerAdmin(admin.ModelAdmin):
    list_display = ['name','email','image','bio']
    ordering = ['name']
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(PupaVolunteer, PupaVolunteerAdmin)
admin.site.register(Contact, ContactAdmin)

