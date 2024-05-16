from django.shortcuts import render, HttpResponse
from .models import hotel, quarto
from . import nome

 # Create your views here.
def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def reserve(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'reserve.html', context)

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data["nome"]
            var_email = fomr.cleaned_data['email']

            return HttpResponse("<h1>Deu certo</h1>")
    else:
        form = FormNome()

        return render(request, "nome.html", {"form": form})
