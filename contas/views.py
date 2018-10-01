from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
	descricao = "uma desc dinamica com dataBiding"
	return render(request, "contas/home.html", {"des":descricao})
def login(request):
	return HttpResponse("Pagina de login")
def registro(request):
	return HttpResponse("pagina de registros")