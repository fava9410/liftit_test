from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import register_owner_form, register_vehicle_form
from .models import Type_Document, Vehicle_Type, Vehicle_Brand, Vehicle, Owner

def home(request):
    context = {}
    return render(request,"index.html",context)

def about(request):
    context = {}
    return render(request,"about-us.html", context)

@csrf_exempt
def register_owner(request):
	tp = Type_Document.objects.all()
	context = {}
	context['types_document'] = tp

	if request.method == 'POST':
		form = register_owner_form(request.POST or None)
		print("eoeoeoe")
		if form.is_valid():
			print('hola')
			#form.save()
		else:
			#print(form)
			print(form.errors)

		return render(request,"register_owner.html", context)
	else:
		return render(request,"register_owner.html", context)

@csrf_exempt
def register_vehicle(request):
	vb = Vehicle_Brand.objects.all()
	vt = Vehicle_Type.objects.all()
	context = {}
	context['vehicle_brands'] = vb
	context['vehicle_types'] = vt

	if request.method == 'POST':
		form = register_vehicle_form(request.POST or None)
		print("eoeoeoe")
		if form.is_valid():
			print('hola')
			#form.save()
		else:
			print(form)
			print(form.errors)

		return render(request,"register_vehicle.html", context)
	else:
		return render(request,"register_vehicle.html", context)

@csrf_exempt
def check_license_plate(request):
	license_plate = request.POST.get("license_plate")

	if Vehicle.objects.filter(license_plate=license_plate).exists():
		return HttpResponse(True)
	else:
		return HttpResponse(False)