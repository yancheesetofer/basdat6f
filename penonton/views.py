from django.shortcuts import render

# Create your views here.


def pilih(request):
    return render(request, "pilihStadium.html")


def listWaktuStadium(request):
    return render(request, "listWaktuStadium.html")


def listPertandinganStadium(request):
    return render(request, "listPertandinganStadium.html")


def tiketPertandingan(request):
    return render(request, "beliTiket.html")


def listSemuaPertandingan(request):
    return render(request, "listSemuaPertandingan.html")
