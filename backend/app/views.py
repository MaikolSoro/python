from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# mvc
# MVT

def index(request):
	template = """
		<h1>Inicio</h1>
	"""
	return render(request, 'index.html')
def app(request):
	return HttpResponse("Hola mundo Django!!")

def hola_mundo(request):
	return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

	if redirigir == 1:
		return redirect('contacto', nombre ='Maikol', apeliidos="Soro Zúñiga")
	
	return render(request, 'pagina.html')
	

