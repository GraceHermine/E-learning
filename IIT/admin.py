from django.contrib import admin
from .models import Etudiant, Forum, Cours, Salle, Evaluation, Note, Reclamation

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
        queryset.update(statut="Traité")
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut="En attente")
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'

_register(Reclamation, ReclamationAdmin)

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

class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'heures', 'credits', 'created_at')
    list_display_links = ['titre']
    list_filter = ('credits',)
    search_fields = ('titre',)
    ordering = ['titre', 'credits']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['titre', 'heures', 'credits'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

_register(Cours, CoursAdmin)

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

_register(Salle, SalleAdmin)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('type_evaluation', 'date', 'created_at')
    list_display_links = ['type_evaluation']
    list_filter = ('type_evaluation',)
    search_fields = ('type_evaluation',)
    ordering = ['type_evaluation', 'date']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['type_evaluation', 'date'],
            },
        ),
        (
            'Standards',
            {
                'fields': ['created_at', ]
            }
        ),
    ]

_register(Evaluation, EvaluationAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'note', 'created_at')
    list_display_links = ['etudiant']
    list_filter = ('note',)
    search_fields = ('etudiant',)
    ordering = ['etudiant', 'note']
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            'Infos',
            {
                'fields': ['etudiant', 'note'],
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