from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Departement, Club, Evenement

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'budget', 'statut', 'created_at')
    list_display_links = ['nom']
    list_filter = ('statut',)
    search_fields = ('nom', 'code')
    ordering = ['nom']
    list_per_page = 10
    date_hierarchy = 'created_at'

    fieldsets = [
        ('Infos', {'fields': ['nom', 'code', 'budget']}),
        ('Standards', {'fields': ['statut']}),
    ]

    actions = ('activer', 'desactiver')

    def activer(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    activer.short_description = 'Activer'

    def desactiver(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactiver.short_description = 'Désactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)
    
_register(Departement, DepartementAdmin)


class ClubAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut', 'created_at')
    list_display_links = ['nom']
    list_filter = ('statut',)
    search_fields = ('nom',)
    ordering = ['nom']
    list_per_page = 10
    date_hierarchy = 'created_at'

    fieldsets = [
        ('Infos', {'fields': ['nom', 'description']}),
        ('Standards', {'fields': ['statut']}),
    ]

    actions = ('activer', 'desactiver')

    def activer(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    activer.short_description = 'Activer'

    def desactiver(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactiver.short_description = 'Désactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Club, ClubAdmin)


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'club', 'date', 'lieu', 'statut', 'created_at')
    list_display_links = ['nom']
    list_filter = ('statut', 'club')
    search_fields = ('nom', 'lieu')
    ordering = ['date']
    list_per_page = 10
    date_hierarchy = 'created_at'

    fieldsets = [
        ('Infos', {'fields': ['nom', 'club', 'date', 'lieu']}),
        ('Standards', {'fields': ['statut']}),
    ]

    actions = ('activer', 'desactiver')

    def activer(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    activer.short_description = 'Activer'

    def desactiver(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactiver.short_description = 'Désactiver'


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Evenement, EvenementAdmin)
