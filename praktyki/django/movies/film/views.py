from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_response(request):
    #return HttpResponse("Jakiś tam tekst")
    return render(request, 'filmy.html')