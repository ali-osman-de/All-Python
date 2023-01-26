from django.shortcuts import render
from .models import Category, Movie

# Create your views here.

# kategori_liste = ["macera", "romantik", "dram","bilim kurgu"]
# film_liste = [
#     {
#         "id":1,
#         "film_adi":"film 1",
#         "aciklama":"film 1 aciklama",
#         "resim":"1.png",
#         "anasayfa": True
#     },
#     {
#         "id":2,
#         "film_adi":"film 2",
#         "aciklama":"film 2 aciklama",
#         "resim":"2.png",
#         "anasayfa": False
#     },
#     {
#         "id":3,
#         "film_adi":"film 3",
#         "aciklama":"film 3 aciklama",
#         "resim":"3.png",
#         "anasayfa": False    
#     },
#     {
#         "id":4,
#         "film_adi":"film 4",
#         "aciklama":"film 4 aciklama",
#         "resim":"4.png",
#         "anasayfa": False    
#     }

# ]  

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True)
    }
    return render(request, "index.html", data)


def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all()
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)
