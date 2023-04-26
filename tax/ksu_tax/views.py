from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is a site to calculate tax</h1>')

def result(request, index):
    index = index+index*0.15
    return HttpResponse(f'the result is, {index}')

def taxrate(request):
    T = str('15%')
    context = {'tax_rate':T}
    return render(request,"ksu_tax/taxrate.html", context)


