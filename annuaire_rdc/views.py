from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Entreprise

# Create your views here.


def recherche(request):
    query = request.GET.get("q", "")

    entreprises = Entreprise.objects.all()

    if query:
        entreprises = entreprises.filter(
            denomination__icontains=query
        )

    #  CONTEXT TOUJOURS DÉFINI
    context = {
        "entreprises": entreprises,
        "query": query,
    }

    #  Requête HTMX → on retourne UNIQUEMENT les résultats
    if request.headers.get("HX-Request"):
        return render(request, "entreprises/_resultats.html", context)

    #  Chargement normal de la page
    return render(request, "entreprises/recherche.html", context)

 

def detail_entreprise(request, id):
    entreprise = get_object_or_404(Entreprise, id=id)
    return render(request, "entreprises/detail.html", {
        "entreprise": entreprise
    })