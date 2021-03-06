import csv
import random
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .forms import register_owner_form, register_vehicle_form
from .models import Type_Document, Vehicle_Type, Vehicle_Brand, Vehicle, Owner
from .serializer import VehicleSerializer

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
		form = register_owner_form(request.POST, request.FILES)
		print(request.FILES)
		if form.is_valid():
			form.save()
		return render(request,"register_owner.html", context)
	else:
		return render(request,"register_owner.html", context)

@csrf_exempt
def register_vehicle(request):
	vb = Vehicle_Brand.objects.all().order_by('name')
	vt = Vehicle_Type.objects.all().order_by('name')
	context = {}
	context['vehicle_brands'] = vb
	context['vehicle_types'] = vt

	if request.method == 'POST':
		form = register_vehicle_form(request.POST or None)
		if form.is_valid():
			form.save()

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

@csrf_exempt
def check_owner(request):
	owner_document = request.POST.get("number_document")

	if Owner.objects.filter(number_document=owner_document).exists():
		return HttpResponse(True)
	else:
		return HttpResponse(False)

def vehicles_by_brand_report(request):
	total_vehicles = Vehicle.objects.all().count()
	total_brands = Vehicle_Brand.objects.all().order_by('name')
	data = []
	for tb in total_brands:
		color = random.randint(1,4)
		vehicle_by_brand_count = Vehicle.objects.filter(brand = tb).count()
		data.append({'brand': tb.name,
					 'amount': '%s/%s' % (vehicle_by_brand_count,total_vehicles),
					 'percentage': str(round(((vehicle_by_brand_count/total_vehicles)*100),2)),
					 'color':color})

	context = {}
	context['datatable'] = data
	return render(request, "vehicles_by_brand_report.html", context)

def list_vehicles_by_brand_report(request):
	context = {}
	total_brands = Vehicle_Brand.objects.all().order_by('name')
	context['brands'] = total_brands
	return render(request, "list_vehicles_by_brand_report.html", context)

class filter_vehicles_by_brand(generics.ListAPIView):
	serializer_class = VehicleSerializer

	def get_queryset(self):
		brand = self.kwargs['brand']
		return Vehicle.objects.filter(brand_id=brand)

def export_report_to_csv(request):
	vehicles = Vehicle.objects.all()
	response = HttpResponse(content_type="text/csv")
	response["Content-Disposition"] = "attachment; filename='vehicles.csv'"

	writer = csv.writer(response,delimiter=",")
	writer.writerow(["License Plate","Brand","Type","Owner's Type Document", "Owner's Number Document"])

	for vehicle in vehicles:
		writer.writerow([vehicle.license_plate, vehicle.brand.name, vehicle.type.name, vehicle.owner.type_document.name, vehicle.owner.number_document])

	return response
