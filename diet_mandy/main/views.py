from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Home Page
def index(request):
    return render(request, 'index.html')

# Login Page
from django.contrib.auth import authenticate, login

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Signup Page

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

def signup_page(request):
    if request.method == "POST":
        name = request.POST["fullname"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Split name safely
        parts = name.split(" ", 1)
        firstname = parts[0]
        lastname = parts[1] if len(parts) > 1 else ""

        # STEP 1: Check if user already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "Account already exists. Please log in.")
            return redirect('login')

        # STEP 2: Use create_user (this hashes password automatically)
        new_user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname
        )

        # Optional: record login time
        new_user.last_login = timezone.now()
        new_user.save()

        # Auto login after signup
        login(request, new_user)
        messages.success(request, "Account created successfully!")
        return redirect('index')

    return render(request, 'signup.html')



# Pages
@login_required
def calculator(request):
    return render(request, 'calculator.html')

def blogs(request):
    return render(request, 'blogs.html')

def weight_calculator(request):
    return render(request, 'weight_calculator.html')

def Diabetic_Friendly_Diet(request):
    return render(request, 'Diabetic_Friendly_Diet.html')

def kietos(request):
    return render(request, 'kietos.html')

def muscle_gain_diet(request):
    return render(request, 'muscle_gain_diet.html')

def Pcod_diet(request):
    return render(request, 'Pcod_diet.html')

def inquiry_success(request):
    return render(request, "inquiry_success.html")

def blog_1(request):
    return render(request, "blog_1.html")

def blog_2(request):
    return render(request, "blog_2.html")

def blog_3(request):
    return render(request, "blog_3.html")

def blog_4(request):
    return render(request, "blog_4.html")

def blog_5(request):
    return render(request, "blog_5.html")

def blog_6(request):
    return render(request, "blog_6.html")

def blog_7(request):
    return render(request, "blog_7.html")  

def blog_8(request):
    return render(request, "blog_8.html")


#  Inquiry Form (Save + Send Mail)
def inquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        goal = request.POST.get("goal")
        food = request.POST.get("food")
        routine = request.POST.get("routine")

        message = f"""
New Diet Inquiry

Name: {name}
Phone: {phone}
Email: {email}
Age: {age}
Gender: {gender}
Goal: {goal}
Food Preference: {food}

Routine / Eating Habits:
{routine}
"""

        send_mail(
            subject="New Diet Consultation Inquiry",
            message=message,
            from_email=email,
            recipient_list=["deshmukjatin804@gmail.com"],
        )

        return redirect("inquiry-success")

    return render(request, "inquiry_form.html")

