from django.shortcuts import render

def home(request):
    context = {}
    #menus = {'index':'','about':'about'}
    #context['menus'] = menus
    return render(request,"index.html",context)

def about(request):
    context = {}
    return render(request,"about-us.html", context)
