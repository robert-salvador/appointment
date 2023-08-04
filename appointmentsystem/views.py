from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db import transaction
from django.conf import settings
from datetime import datetime, timedelta
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only
import json

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        # Clear any existing messages
        messages.get_messages(request)

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    else:
        # Clear any existing messages
        messages.get_messages(request)

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'accounts/dashboard.html') 

@login_required(login_url='login')
def booking(request):
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(31)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    # Get all services from the database
    services = service.objects.all()
    complementary_drinks = complementarydrink.objects.all()
    picked_barber = barber.objects.all()
    add_drinks = beverage.objects.all()

    if request.method == 'POST':
        service_id = request.POST.get('service')
        complementary_drink_id = request.POST.get('complementary_drink')
        picked_barber_id = request.POST.get('picked_barber')
        additional_drink_ids = request.POST.getlist('additional_drinks')
        day = request.POST.get('day')
        if service_id is None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking')

        # Store day, service ID, and picked barber in Django session:
        request.session['day'] = day
        request.session['service_id'] = service_id
        request.session['complementary_drink_id'] = complementary_drink_id
        request.session['picked_barber_id'] = picked_barber_id
        request.session['additional_drink_ids'] = additional_drink_ids

        return redirect('bookingSubmit')

    return render(request, 'accounts/booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'services': services,  # Pass the services to the template
        'complementary_drinks': complementary_drinks,
        'picked_barber': picked_barber,
        'add_drinks': add_drinks,
    })

@login_required(login_url='login')
def bookingSubmit(request):
    user = request.user
    times = [
        "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from Django session:
    add_drinks = beverage.objects.all()
    day = request.session.get('day')
    service_id = request.session.get('service_id')
    complementary_drink_id = request.session.get('complementary_drink_id')
    picked_barber_id = request.session.get('picked_barber_id')
    additional_drink_ids = request.POST.getlist('additional_drinks')

    # Retrieve the service object from the database using the ID
    service_obj = get_object_or_404(service, pk=service_id)
    complementary_drink_obj = None
    if complementary_drink_id:
        complementary_drink_obj = get_object_or_404(complementarydrink, pk=complementary_drink_id)
    picked_barber_obj = get_object_or_404(barber, pk=picked_barber_id)
    additional_drinks = beverage.objects.filter(pk__in=additional_drink_ids)

    # Only show the time of the day that has not been selected before:
    hour = checkTime(times, day, picked_barber_obj)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service_obj is not None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday' or date == 'Saturday' or date == 'Sunday':
                    if AppointmentNew.objects.filter(day=day, chosen_barber=picked_barber_obj).count() < 11:
                            if AppointmentNew.objects.filter(day=day, time=time, chosen_barber=picked_barber_obj).count() < 1:
                                appointment_obj, created = AppointmentNew.objects.get_or_create(
                                    user = user,
                                    service = service_obj,
                                    corresponding_drink = complementary_drink_obj,
                                    chosen_barber = picked_barber_obj,
                                    day = day,
                                    time = time,
                                )
                                appointment_obj.additional_drinks.clear()  # Clear existing drinks
                    
                                for additional_drink in additional_drinks:
                                    appointment_obj.additional_drinks.add(additional_drink)

                                # Prepare the message for the email
                                subject = 'Appointment Confirmation'
                                message = f'Hello {user.username},'
                                message += f'Your appointment has been booked for {day} at {time}. Please show this email when you arrive. '
                                message += f'\nService: {service_obj.name} - PHP {service_obj.price}'

                                if complementary_drink_obj is not None:
                                    message += f'\nComplementary Drink: {complementary_drink_obj.name}'
                                else:
                                    message += '\nComplementary Drink: None'

                                message += f'\nBarber: {picked_barber_obj.name}'
                                message += '\nAdditional Drinks:'
                                for additional_drink in additional_drinks:
                                    message += f'\n- {additional_drink.name} - PHP {additional_drink.price}'
                                message += '\n\nThank you for booking with us!'
                                from_email = settings.DEFAULT_FROM_EMAIL
                                recipient_list = [user.email]

                                try:
                                    send_mail(subject, message, from_email, recipient_list)
                                    messages.success(request, "Appointment Saved! An email confirmation has been sent.")
                                except Exception as e:
                                    messages.error(request, "Failed to send email confirmation. Please check your email settings.")

                                return redirect('home')
                            else:
                                messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")


    return render(request, 'accounts/bookingsubmit.html', {
        'times': hour,
        'add_drinks': add_drinks,
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 31 days from today
    items = AppointmentNew.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'accounts/staffPanel.html', {
        'items':items,
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def delete_appointment(request, appointment_id):
    # Get the appointment object to be deleted
    appointment = get_object_or_404(AppointmentNew, id=appointment_id)

    # Add any additional logic to check if the appointment can be deleted (e.g., check if it's not already completed)

    # Delete the appointment
    appointment.delete()

    # Optionally, you can add a success message here to show to the user
    messages.success(request, "Appointment deleted successfully.")

    return redirect('staffPanel')

def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    #Loop days you want 
    today = datetime.now()
    weekdays = []
    for i in range (1, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if AppointmentNew.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day, picked_barber_obj):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if AppointmentNew.objects.filter(day=day, time=k, chosen_barber=picked_barber_obj).count() < 1:
            x.append(k)
    return x
