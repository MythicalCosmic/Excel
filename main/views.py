from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def main(request):
    query = request.GET.get('q')
    
    if query:
        users = User.objects.filter(full_name__icontains=query).order_by('-created_at')
    else:
        users = User.objects.all().order_by('-created_at')

    users_count = users.count()
    paginator = Paginator(users, 6)  
    page_number = request.GET.get('page', '1')
    page_obj = paginator.get_page(page_number)

    context = {
        'users_count': users_count,
        'users': page_obj,
        'query': query,  
    }
    
    return render(request, "main.html", context)

@login_required
def createUser(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        birthdate = request.POST.get('birthdate')
        address = request.POST.get('address')
        street = request.POST.get('street')
        passport_number = request.POST.get('passport_number')
        passport_letter = request.POST.get('passport_letter')
        status = request.POST.get('status')
        new_user = User(full_name=full_name, phone_number=phone_number, birthdate=birthdate, address=address, street=street, passport_number=passport_number, passport_letter=passport_letter, status=status)
        new_user.save()
        return redirect("main")
    else:
        return render(request, "main.html")
    
@login_required
def deleteAll(request):
    User.objects.all().delete()
    return redirect("main")

@login_required
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        print(f"Request User ID: {pk}")
        print(request.POST)
        user.full_name = request.POST.get('full_name', user.full_name)
        user.phone_number = request.POST.get('phone_number', user.phone_number)
        user.birthdate = request.POST.get('birthdate', user.birthdate)
        user.address = request.POST.get('address', user.address)
        user.street = request.POST.get('street', user.street)
        user.passport_number = request.POST.get('passport_number', user.passport_number)
        user.passport_letter = request.POST.get('passport_letter', user.passport_letter)
        user.status = request.POST.get('status', user.status)

        try:
            user.save()
            return redirect('main')  
        except Exception as e:
            return HttpResponseBadRequest(f"An error occurred: {e}")

    return render(request, 'main.html', {'user': user})

@login_required
def delete_user(request, pk):
    if request.method == 'POST':
        try:
            user = get_object_or_404(User, pk=pk)
            user.delete()
            print(f"User with id {pk} deleted successfully.")
            return redirect('main')  
        except Exception as e:
            return redirect('main')  
    else:
        print("Request method is not POST.")
        return render(request, 'main.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('main') 
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('main') 