from django.shortcuts import render
from .models import Artigo
from django.db.models import Q
# Create your views here.
def home(request):

    artigos = Artigo.objects.all()
    quant = len(artigos)

    return render(request, 'home.html', {"quant": quant, "artigos": artigos})

def search(request):
    query = request.GET.get('search')
    result = Artigo.objects.filter(Q(titulo__contains=query) | Q(editor__iexact=query) | Q(palavras_chaves__contains=query))

    return render(request, 'search.html', {'result': result})

# def search(request):
#     if request.method == 'GET':
#         result = request.GET.get('search')
#         try:
#             status = Artigo.objects.filter(titulo=result)
#         except:
#             pass
#         return render(request, 'search.html', {"result":status})
#     else:
#         return render(request,'search.html',{})