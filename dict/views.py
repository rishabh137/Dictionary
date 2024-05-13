from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def search(request):
    search = request.GET.get("search")
    return render(request, "search.html")
