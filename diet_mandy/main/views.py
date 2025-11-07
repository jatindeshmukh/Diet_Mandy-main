from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# @login_required
def index(request):    
    return render(request, 'index.html')

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("Login attempt:", email)  # Debug print
        
        try:
            # First get the user with this email
            user = User.objects.filter(email=email).first()
            if user is not None:
                print("----------------User Found-----------------" + user.username, user.email, user.password)
                # Try to authenticate with username (email) and password
                # authenticated_user = authenticate(request, username=user.username, password=password)
                # if authenticated_user is not None:
                #     print("----------------Login Successful-----------------")
                # else:
                #     print("Authentication failed for user:", email)
                if password == user.password: # For now checking password manually without the authenticate function as it seems not working
                    login(request, user)
                    return redirect('index')
                else:
                    raise ValueError("Invalid password")
            else:
                print("No user found with this email:", email)
                
        except Exception as e:
            print("Login error:", str(e))
            print("Redirecting to login page again.")
        
        return redirect('login')

    if request.method == "GET":
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_page(request):
    if request.method == "POST":
        print("--------------Here-------------------------")
        name = request.POST["fullname"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstname, lastname, *extra = name.split(" ")
        print("Form received:", name)  # just to confirm in your terminal
        
        # Create user with create_user to properly hash the password
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
        messages.success(request, "Account created successfully! Please login.")
        return redirect('index')
    if request.method == "GET":
        print("-------------------Get method-----------------------")
        return render(request, 'signup.html')

@login_required
def calculator(request):       
    return render(request, 'calculator.html')


def blogs(request):       
    return render(request, 'blogs.html')

def weight_calculator(request):       
    return render(request, 'weight_calculator.html')



# def muscle_gain_diet(request):
#     return render(request, 'muscle_gain_diet.html') 

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        primary_goal = request.POST['primary_goal']
        diet_type = request.POST['diet_type']
        allergies = request.POST['allergies']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # Create User
        user = User.objects.create_user(username=email, email=email, password=password)

        # Save profile
        Profile.objects.create(
            user=user,
            full_name=full_name,
            contact_number=contact_number,
            age=age,
            gender=gender,
            height=height,
            primary_goal=primary_goal,
            diet_type=diet_type,
            allergies=allergies
        )

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'signup.html')

def  Diabetic_Friendly_Diet(request):       
    return render(request, 'Diabetic_Friendly_Diet.html')

def kietos(request):       
    return render(request, 'kietos.html')

def muscle_gain_diet(request):
    return render(request, 'muscle_gain_diet.html')

def Pcod_diet(request):
    return render(request, 'Pcod_diet.html')

def inquiry(request):
    return render(request, 'Inquiry.html')
    


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
