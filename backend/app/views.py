from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# mvc
# MVT

def index(request):
	template = """
		<h1>Inicio</h1>
	"""
	name = 'Michael'
	languages = ['JavaScript', 'Python', 'PHP', 'Typescript']

	return render(request, 'index.html', {
		'title' : 'Inicio',
		'mi_variable': 'Soy un dato que está en la vista',
		'name': name,
		'languages': languages
	})

def app(request):
	return HttpResponse("Hola mundo Django!!")

def hola_mundo(request):
	return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

	if redirigir == 1:
		return redirect('contacto', nombre ='Maikol', apeliidos="Soro Zúñiga")
	
	return render(request, 'pagina.html')
	

