from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# mvc
# MVT

def index(request):
	template = """
		<h1>Inicio</h1>
	"""
	return HttpResponse(template)
def app(request):
	return HttpResponse("Hola mundo Django!!")

def pagina(request, redirect=0):
	return redirect('/inicio/')
	return HttpResponse("""
		<h1>Página de mi web </h1>
	""")
