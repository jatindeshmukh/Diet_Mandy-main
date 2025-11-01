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
