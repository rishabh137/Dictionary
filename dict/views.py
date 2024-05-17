from django.shortcuts import render
import requests
import bs4

# from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, "index.html")


def search(request):
    search = request.GET.get("search")
    res = requests.get("https://www.dictionary.com/browse/" + search)  # for meaning
    res2 = requests.get(
        "https://www.thesaurus.com/browse/" + search
    )  # for antonym and synonym
    res3 = requests.get("https://www.antonym.com/antonyms/" + search)

    if res:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        meaning = soup.find_all("div", {"class": "NZKOFkdkcvYgD3lqOIJw"})
        meaning1 = meaning[0].getText()
    else:
        search = "Sorry, " + search + " Is Not Found In Our Database"
        meaning = ""
        meaning1 = ""

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, "html.parser")

        synonyms = soup2.select(".fltPJVdHfRCxJJVuGX8J a")
        ss = []
        for b in synonyms[0:5]:
            re = b.text.strip()
            ss.append(re)
        se = ss
    else:
        se = ""

    if res3:
        soup2 = bs4.BeautifulSoup(res3.text, "html.parser")

        antonyms = soup2.select(".section-list > .chip a")
        aa = []
        for a in antonyms[0:5]:
            re = a.text.strip()
            aa.append(re)
        ae = aa
    else:
        ae = ""

    results = {
        "search": search,
        "meaning": meaning1,
    }
    return render(request, "search.html", {"se": se, "ae": ae, "results": results})
