from django.contrib import admin
from .models import Entreprise


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration du modèle Entreprise
    """

    # Colonnes affichées dans la liste
    list_display = (
        "sigle",
        "denomination",
        "secteursactivite",
        "telephone",
        "email",
        "created_at",
    )

    # Barre de recherche en haut
    search_fields = (
        "sigle",
        "denomination",
        "secteursactivite",
        "adresse",
        "description",
    )

    # Filtres sur le côté droit
    list_filter = (
        "secteursactivite",
        "created_at",
    )

    # Organisation du formulaire (ajout / modification)
    fieldsets = (
        ("Informations générales", {
            "fields": (
                "sigle",
                "denomination",
                "description",
                "secteursactivite",
            )
        }),

        ("Coordonnées", {
            "fields": (
                "telephone",
                "email",
                "adresse",
                "villescouvertes",
                "siteweb",
            )
        }),

        ("Média", {
            "fields": (
                "photo",
            )
        }),

        ("Métadonnées", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    # Champs en lecture seule
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # Pagination
    list_per_page = 20

    # Tri par défaut
    ordering = ("-created_at",)

    # Amélioration UX
    save_on_top = True
