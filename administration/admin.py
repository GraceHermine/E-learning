from django.contrib import admin
from .models import Administrateur,Bibliothcaire,Inscription,Livre, EnseignantB, Bibliotheque
# Register your models here.

# class EmploiDuTempsAdmin(admin.ModelAdmin):
#     list_display = ('get_enseignant_nom', 'matiere', 'jour', 'heure_debut', 'heure_fin', 'specialite', 'niveau', 'classe', 'statut', 'created_at')

#     list_display_links = ['get_enseignant_nom', 'matiere']

#     list_filter = ('statut', 'specialite', 'niveau', 'classe', 'enseignant', 'jour')

#     search_fields = ('enseignant__nom', 'matiere', 'jour', 'specialite', 'niveau', 'classe')

#     ordering = ['jour', 'heure_debut']

#     list_per_page = 10

#     date_hierarchy = 'created_at'

#     fieldsets = [
#         (
#             'Informations sur le cours', 
#             {
#                 'fields': ['enseignant', 'matiere', 'specialite']
#             }
#         ),
#         (
#             'Horaire', 
#             {
#                 'fields': ['jour', 'heure_debut', 'heure_fin']
#             }
#         ),
#         (
#             'Classe', 
#             {
#                 'fields': ['niveau', 'classe']
#             }
#         ),
#         (
#             'Statut', 
#             {
#                 'fields': ['statut']
#             }
#         ),
#     ]

#     def get_enseignant_nom(self, obj):
#         return obj.enseignant.nom
#     get_enseignant_nom.short_description = 'Enseignant'
#     get_enseignant_nom.admin_order_field = 'enseignant__nom'

#     actions = ('active', 'desactive')

#     def active(self, request, queryset):
#         queryset.update(statut=True)
#         self.message_user(request, 'La sélection a été activée avec succès')
#     active.short_description = 'Activer'

#     def desactive(self, request, queryset):
#         queryset.update(statut=False)
#         self.message_user(request, 'La sélection a été désactivée avec succès')
#     desactive.short_description = 'Désactiver'
# def _register(model, admin_class):
#     admin.site.register(model, admin_class)

# _register(EmploiDuTemps, EmploiDuTempsAdmin)



class EnseignantAdmin(admin.ModelAdmin):

    list_display = ('user', 'matricule', 'nom', 'prenom', 'email', 'telephone', 'grade', 'departement', 'created_at')

    list_display_links = ['nom',]

    list_filter = ('departement',)

    search_fields = ('nom',)

    date_hierarchy = 'created_at'

    ordering = ['matricule', 'nom', 'grade', 'departement']
    
    list_per_page = 10

    fieldsets = [
            (
                'Informations personnelles', 
                {
                    'fields': [ 'user', 'matricule', 'nom', 'prenom', 'email', 'telephone'],
                },
            ),
              (
                'Informations relatives au cours dispensés', 
                {
                    'fields': ['grade', 'departement'],
                },
            ),
         
            ]

    actions = ('active','desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La selection a été activé avec succès')

    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La selection a été désactivé avec succès')

    desactive.short_description = 'Desactiver'


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(EnseignantB, EnseignantAdmin)



















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


class BibliothcaireAdmin(admin.ModelAdmin):
    list_display = (  'nom' , 'adresse', 'telephone', 'statut', 'created_at')

    list_display_links = ['adresse',]

    list_filter = ('statut',)

    search_fields = ('adresse',)

    ordering = ['adresse',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Informations sur le/la bibliothécaire', 
                {
                    'fields': ['nom', 'telephone','adresse'],
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

_register(Bibliothcaire, BibliothcaireAdmin)


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
                    'fields': ['utilisateur'],
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
    list_display = ('isbn', 'titre' , 'resume', 'nombre_de_page', 'edition', 'auteur', 'categorie', 'date_publication','statut', 'created_at')

    list_display_links = ['isbn',]

    list_filter = ('statut',)

    search_fields = ('isbn',)

    ordering = ['isbn',]

    list_per_page = 10

    date_hierarchy = 'created_at'

    fieldsets = [
            (
                'Information sur le livre', 
                {
                    'fields': ['isbn', 'titre', 'resume', 'nombre_de_page', 'edition', 'auteur', 'categorie', 'date_publication'],
                },
            ),
            (
                'Couverture du livre',
                {
                    'fields': ['couverture'],
                }, 
               
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


class BibliothequeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'responsable', 'telephone', 'statut', 'created_at')
    
    def has_add_permission(self, request):
        # Empêche l'ajout si une bibliothèque existe déjà
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Empêche la suppression de la bibliothèque
        return False

    fieldsets = [
        (
            'Informations sur la bibliothèque', 
            {
                'fields': ['nom', 'responsable', 'telephone', 'adresse'],
            },
        ),
        (
            'Livres', 
            {
                'fields': ['livres'],
            },
        ),
        (
            'Statut', 
            {
                'fields': ['statut'],
            },
        ),
    ]

    def save_model(self, request, obj, form, change):
        if not change:  # Si c'est une nouvelle instance
            obj.nom = "Bibliothèque du site"  # Force le nom
        super().save_model(request, obj, form, change)

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Bibliotheque, BibliothequeAdmin)