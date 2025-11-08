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
def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email=email).first()
        if user and password == user.password:  # ⚠ Simplified auth (not secure)
            login(request, user)
            return redirect('index')
        return redirect('login')

    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Signup Page
def signup_page(request):
    if request.method == "POST":
        name = request.POST["fullname"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstname, lastname, *extra = name.split(" ")

        new_user = User.objects.create(
            username=email,
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname
        )
        new_user.last_login = timezone.now()
        new_user.save()
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


# ✅ Success Page
def inquiry_success(request):
    return render(request, "inquiry_success.html")

# from django.shortcuts import render, redirect
# from django.http import HttpResponse

# def save_profile(request):
#     if request.method == "POST":
#         fullname = request.POST.get("fullname")
#         contact = request.POST.get("contact")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirmPassword")
#         age = request.POST.get("age")
#         gender = request.POST.get("gender")
#         height = request.POST.get("height")
#         goal = request.POST.get("goal")
#         dietType = request.POST.get("dietType")
#         allergies = request.POST.get("allergies")

        # 👇 yaha aap database save kar sakte ho
        # Example:
        # UserProfile.objects.create(...)

    #     return HttpResponse(" Profile Saved Successfully!")

    # return HttpResponse("Invalid Request")
