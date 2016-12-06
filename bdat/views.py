from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from .models import Institution, Technology


# Create your views here.

def home(request):
    queryset = Technology.objects.all()
    list = [entry for entry in queryset]
    return render(request, "home.html", {'attributs': list})


def category(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.cat_assistance for entry in queryset], "titre": "Assistance",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def categories(request):
    return render_to_response("categories.html")


def about(request):
    return render_to_response("about.html")


def contact(request):
    return render_to_response("contact.html")


def search_cat():
    """
    search_cat propose une page permettant à l'utilisateur de selectionner
    par une suite de listes déroulantes
    :return:
    """


def categorya(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.cat_assistance for entry in queryset], "titre": "Assistance",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def categoryf(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.cat_fonctions for entry in queryset], "titre": "Fonctions",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def categoryt(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.cat_techno for entry in queryset], "titre": "Technologies",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def technology(request):
    queryset = Technology.objects.all()

    return render(request, "techno.html",
                  {"att": queryset[0]})


def technology_(request):
    queryset = Technology.objects.all()

    return render(request, "techno.html",
                  {"att": queryset[1]})