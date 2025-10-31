from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print("Form received:", name)  # just to confirm in your terminal
        context = {'message': f'Thank you, {name}!' if name else 'Form submitted!'}
        return render(request, 'index.html', context)
    
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')


def calculator(request):       
    return render(request, 'calculator.html')


def blogs(request):       
    return render(request, 'blogs.html')

def weight_calculator(request):       
    return render(request, 'weight_calculator.html')