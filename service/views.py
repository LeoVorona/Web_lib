from re import template
from django.http import HttpResponse, Http404, FileResponse, JsonResponse

from .models import Product

from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template

from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')
    
def page(request, page_num):
    return HttpResponse(f'Page {page_num}')

def about(request, id):

    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist :
        raise Http404("NOT FOUND")
    return HttpResponse('OK')

def file_show(request):
    file = 'service/image.jpg'
    return FileResponse(open(file, 'rb'))

def json_show(request):
    data = {'cost':14, 'title':'book'}
    return JsonResponse(data)