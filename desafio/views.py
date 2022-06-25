from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Familiar

# Create your views here.
def inicio (request):
    return render(request,'index.html')

def un_template(request):
    
#    template = loader.get_template('index.html')
    
    familiar1 = Familiar(nombre='Juan',edad= 34,fecha_nacimiento= '1987-7-14')
    familiar2 = Familiar(nombre='Horacio',edad= 2, fecha_nacimiento= '2000-2-20')
    familiar3 = Familiar(nombre='Ricardo',edad= 31, fecha_nacimiento= '1991-5-19')
    
    familiar1.save()
    familiar2.save()
    familiar3.save()

#    render = template.render({'lista_familiar': [familiar1, familiar2, familiar3]})
#    return HttpResponse(render)

    return render(request,'mi_template.html', {'lista_familiar': [familiar1, familiar2, familiar3]})