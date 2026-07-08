from django.shortcuts import render, redirect , get_object_or_404
from user.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import JobPost
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')
    return render(request, 'signup.html')

def employeer_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        company = request.POST.get('company')
        company_profile = request.POST.get('company_profile')

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            company=company,
            company_profile=company_profile,
            role="employeer"
        )
        return redirect('employer-login')
    return render(request, 'employer-signup.html')

def employeer_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == "employeer":
                login(request, user)
                return redirect("employer-dashboard")  # Change to your dashboard URL name
            else:
                messages.error(request, "You are not registered as an employer.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "employer-login.html")

def landing_page(request):
    jobs = JobPost.objects.all()
    return render(request, 'landing_page.html', {'jobs': jobs})

@login_required
def applicant_dashboard(request):
    return render(request, 'applicant/applicant-dashboard.html')

@login_required
def employer_dashboard(request):
    return render(request, 'employeer/employer-dashboard.html')

@login_required
def employer_job_list(request):
    # Restrict access to employers only
    if request.user.role != "employeer":
        return redirect("employer-login")

    jobs = JobPost.objects.filter(employer=request.user).order_by("-created_at")

    return render(request, "employeer/job_list.html", {
        "jobs": jobs
    })

@login_required
def employer_job_post(request):
    # Only allow employers
    if request.user.role != "employeer":
        return redirect("employer-login")

    if request.method == "POST":
        JobPost.objects.create(
            employer=request.user,
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            salary=request.POST.get("salary"),
            location=request.POST.get("location"),
            job_type=request.POST.get("job_type"),
            is_available=True,
        )
        return redirect("job-list")

    return render(request, "employeer/job_post.html")

@login_required
def toggle_job_status(request, job_id):
    job = get_object_or_404(
        JobPost,
        id=job_id,
        employer=request.user
    )

    job.is_available = not job.is_available
    job.save()

    return redirect("job-list")

def employee_logout(request):
    logout(request)
    return redirect('employer-login')