from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import register_owner

def home(request):
    context = {}
    #menus = {'index':'','about':'about'}
    #context['menus'] = menus
    return render(request,"index.html",context)

def about(request):
    context = {}
    return render(request,"about-us.html", context)

@csrf_exempt
def register_owner(request):
	if request.method == 'POST':		
		
		#form = register_owner(request.POST)
		print("eoeoeoe")
		#if form.is_validate():
		#	print('hola')
		return render(request,"register_owner.html", {})
	else:
		context = {}
		return render(request,"register_owner.html", context)