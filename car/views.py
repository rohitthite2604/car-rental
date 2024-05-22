from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def form(request):
    return render(request, '\\form.html')

def registered(request):
    first_name = request.POST['fn']
    last_name = request.POST['ln']
    email = request.POST['email']
    password = request.POST['password']
    
    person = Registration(first_name=first_name, last_name=last_name, email=email, password=password)
    person.save()
    return render(request, 'car/registered.html', {'fn':first_name})

from django.http import HttpResponse
from django.shortcuts import render

from car.models import Contact

# Create your views herev python functions.


def home(request):

    if request.method=="POST":
        contact = Contact()
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphone = request.POST.get('phone')
        fcontent = request.POST.get('content')
        contact.name = fname
        contact.email = femail
        contact.phone = fphone
        contact.content = fcontent
        contact.save()
        return HttpResponse(" Data is saved Successfully")

    # return HttpResponse("This Is a car rental website")
    return render(request,'page2.html')

def car(request):
    return render(request, 'car.html')

def book_car(request, car_id):
    if request.method == 'POST':
        car = Car.objects.get(pk=car_id)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        user_name = request.POST['user_name']
        user_email = request.POST['user_email']
        booking = Booking.objects.create(car=car, start_date=start_date, end_date=end_date, user_name=user_name, user_email=user_email)
        return redirect('home')
    else:
        car = Car.objects.get(pk=car_id)
        return render(request, 'book.html', {'car': car})