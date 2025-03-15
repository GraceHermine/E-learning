from django.contrib import admin
from .models import EmploiDuTemps,Enseignant,Administrateur,Bibliotheque,Inscription,Livre
# Register your models here.

class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('jour', 'statut', 'created_at')

    list_display_links = ['jour',]

    list_filter = ('statut',)

    search_fields = ('jour',)

    ordering = ['jour',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Infos', 
                {
                    'fields': ['jour', 'Heure de début'],
                },
            ),
            (
                'Standards', 
                {
                    'fields': ['statut', ]
                }
            ),
            ]

    actions = ('active','desactive')

    def active(self,request,queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactiver avec succès')
    desactive.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(EmploiDuTemps, EmploiDuTempsAdmin)


class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'matricule','departement', 'statut', 'created_at')

    list_display_links = ['nom',]

    list_filter = ('statut',)

    search_fields = ('nom',)

    ordering = ['nom',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Infos', 
                {
                    'fields': ['nom', 'Specialite', 'departement'],
                },
            ),
            (
                'Standards', 
                {
                    'fields': ['statut', ]
                }
            ),
            ]

    actions = ('active','desactive')

    def active(self,request,queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactiver avec succès')
    desactive.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Enseignant, EnseignantAdmin)



class AdministrateurAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'statut', 'created_at')

    list_display_links = ['utilisateur',]

    list_filter = ('statut',)

    search_fields = ('utilisateur',)

    ordering = ['utilisateur',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Infos', 
                {
                    'fields': ['utilisateur', 'role'],
                },
            ),
            (
                'Standards', 
                {
                    'fields': ['statut', ]
                }
            ),
            ]

    actions = ('active','desactive')

    def active(self,request,queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactiver avec succès')
    desactive.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Administrateur, AdministrateurAdmin)


class BibliothequeAdmin(admin.ModelAdmin):
    list_display = ('adresse', 'statut', 'created_at')

    list_display_links = ['adresse',]

    list_filter = ('statut',)

    search_fields = ('adresse',)

    ordering = ['adresse',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Infos', 
                {
                    'fields': ['adresse'],
                },
            ),
            (
                'Standards', 
                {
                    'fields': ['statut', ]
                }
            ),
            ]

    actions = ('active','desactive')

    def active(self,request,queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactiver avec succès')
    desactive.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Bibliotheque, BibliothequeAdmin)


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('utilisateur','date_inscription' ,'statut', 'created_at')

    list_display_links = ['utilisateur',]

    list_filter = ('statut',)

    search_fields = ('utilisateur',)

    ordering = ['utilisateur',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Infos', 
                {
                    'fields': ['utilisateur', 'date_inscription'],
                },
            ),
            (
                'Standards', 
                {
                    'fields': ['statut', ]
                }
            ),
            ]

    actions = ('active','desactive')

    def active(self,request,queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactiver avec succès')
    desactive.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Inscription, InscriptionAdmin)


class LivreAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titre' ,'statut', 'created_at')

    list_display_links = ['isbn',]

    list_filter = ('statut',)

    search_fields = ('isbn',)

    ordering = ['isbn',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Infos', 
                {
                    'fields': ['isbn', 'titre'],
                },
            ),
            (
                'Standards', 
                {
                    'fields': ['statut', ]
                }
            ),
            ]

    actions = ('active','desactive')

    def active(self,request,queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactiver avec succès')
    desactive.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Livre, LivreAdmin)