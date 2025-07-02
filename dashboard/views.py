from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from supabase import create_client
from .supabase_client import supabase  # Ensure this import matches your supabase client setup
from functools import wraps
from django.shortcuts import redirect

def supabase_login_required(view_func):
    """
    Decorator to ensure that the user is logged in via Supabase.
    If not logged in, redirects to the login page.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'access_token' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


# Create your views here
@supabase_login_required
def home(request):
    return render(request, 'dashboard/home.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        # Call supabase login
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if response.session:
            # If login is successful, set the session
            request.session['access_token'] = response.session.access_token
            request.session['refresh_token'] = response.session.refresh_token
            request.session['user_email'] = email

            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'dashboard/login.html', {'form': AuthenticationForm()})
            



def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        #call supabase signup
        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password
            }
        )

        if response.user:
            messages.success(request, 'Account created successfully!, check your email to verify your account.')
            return redirect('login')  # Change 'login' to your desired URL name
        else:
            messages.error(request, 'Error creating account. Please try again.')
    return render(request, 'dashboard/signup.html')