from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def quienes_somos(request):
    return render(request, 'main/quienes_somos.html')