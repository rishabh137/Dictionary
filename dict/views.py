from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, "index.html")


def search(request):
    search = request.GET.get("search")
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)

    context = {"meaning": meaning, "synonym": synonym, "antonym": antonym}

    return render(request, "search.html", context)
