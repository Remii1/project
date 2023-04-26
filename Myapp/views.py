from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def recipe(request):
    return render(request,'recipe.html')
def contact(request):
    return render(request,'contact.html')
