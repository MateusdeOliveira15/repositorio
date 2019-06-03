from django.shortcuts import render
from .models import Artigo
# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    if request.method == 'GET':
        result = request.GET.get('search')
        try:
            status = Artigo.objects.filter(titulo=result)
        except:
            pass
        return render(request, 'search.html', {"result":status})
    else:
        return render(request,'search.html',{})