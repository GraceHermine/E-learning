from django.contrib import admin
from .models import Etudiant, Forum, Reclamation, Cours, Salle, Evaluation, Note,ChatMessage

# Admin pour le modèle Etudiant
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'specialite', 'created_at')
    list_display_links = ['matricule',]
    list_filter = ('specialite',)
    search_fields = ('matricule','specialite')
    ordering = ['matricule']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['matricule', 'niveau', 'specialite'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(Etudiant, EtudiantAdmin)

# Admin pour le modèle Forum
class ForumAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'created_at')
    list_display_links = ['titre']
    list_filter = ('date_creation',)
    search_fields = ('titre',)
    ordering = ['titre', 'date_creation']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['titre', 'date_creation'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

_register(Forum, ForumAdmin)

# Admin pour le modèle Reclamation
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'description', 'statut', 'created_at')
    list_display_links = ['sujet']
    list_filter = ('statut',)
    search_fields = ('sujet', 'description')
    ordering = ['sujet', 'statut']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['sujet', 'description', 'statut'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]
    actions = ('active', 'desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'

_register(Reclamation, ReclamationAdmin)

# Admin pour le modèle Cours
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'group', 'heures', 'credits', 'statut', 'created_at', 'last_updated_at')
    list_display_links = ['titre']
    list_filter = ('credits', 'group', 'statut')
    search_fields = ('titre', 'description')
    ordering = ['titre', 'credits']
    list_per_page = 10
    date_hierarchy = 'created_at'
   

    fieldsets = [
        (
            'Infos',
            {
                'fields': ['titre', 'group', 'heures', 'credits', 'description', 'contenu', 'video_url'],
            },
        ),
       
    ]

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'

admin.site.register(Cours, CoursAdmin)

# Admin pour le modèle Salle
class SalleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'capacite', 'type_salle', 'created_at')
    list_display_links = ['nom']
    list_filter = ('type_salle',)
    search_fields = ('nom',)
    ordering = ['nom', 'type_salle']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['nom', 'capacite', 'type_salle'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'


_register(Salle, SalleAdmin)

# Admin pour le modèle Evaluation
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('cours', 'type_evaluation', 'date', 'created_at')  # Affichage du cours
    list_display_links = ['type_evaluation']
    list_filter = ('type_evaluation', 'cours')  # Ajout du filtre par cours
    search_fields = ('type_evaluation', 'cours__titre')  # Recherche par cours
    ordering = ['cours', 'type_evaluation', 'date']
    list_per_page = 10
    date_hierarchy = 'created_at'
    
    # Mise à jour des champs affichés dans le formulaire d'édition
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['cours', 'type_evaluation', 'date', 'duree'],  # Ajout du champ 'cours'
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'

    
# Enregistrer l'administration personnalisée
admin.site.register(Evaluation, EvaluationAdmin)

# Admin pour le modèle Note
class NoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'valeur', 'created_at')
    list_display_links = ['etudiant']
    list_filter = ('valeur',)
    search_fields = ('etudiant',)
    ordering = ['etudiant', 'valeur']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['etudiant', 'valeur'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

_register(Note, NoteAdmin)



class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    list_display_links = ['user']
    list_filter = ('message',)
    search_fields = ('user',)
    ordering = ['user', 'message']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['user', 'message'],
            },
        ),
        
    ]

_register(ChatMessage, MessageAdmin)

