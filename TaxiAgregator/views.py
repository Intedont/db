from django.shortcuts import render, redirect
from TaxiAgregator.forms import SignUpForm, OrderForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from TaxiAgregator.models import Clients, PaymentDetails, Orders, Drivers, Auto, AutoProperties
from django.db.models import Model
import random
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            last_name = form.cleaned_data.get('lastname')
            print(password)
            user = User.objects.create_user(username=username, last_name=last_name, password=password)
            user.save()
            det = PaymentDetails(card_number=form.cleaned_data.get('card_number'),
                                 cvc=form.cleaned_data.get('cvc'))
            det.save()
            client = Clients(details=det,
                             name=username,
                             last_name=last_name,
                             telephone_number=form.cleaned_data.get('phone'),
                             )
            client.save()

            return redirect('/taxi/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='/taxi/login')
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            dep_lat = form.cleaned_data.get('departure_latitude')
            dep_lon = form.cleaned_data.get('departure_longitude')
            arr_lat = form.cleaned_data.get('arrival_latitude')
            arr_lon = form.cleaned_data.get('arrival_longitude')
            try:
                current_client = Clients.objects.get(name=request.user)
                order = Orders(client=current_client,
                               sum=calculate_sum(),
                               departure_latitude=dep_lat,
                               departure_longitude=dep_lon,
                               arrival_latitude=arr_lat,
                               arrival_longitude=arr_lon,
                               driver=Drivers.objects.get(driver_id=find_driver()),
                               state=1)
                order.save()
            except Model.DoesNotExist:
                print("Client not found")

            return redirect('/taxi/check_order')
    else:
        form = OrderForm()
        context = {
            'username': get_user(request).username
        }
        return render(request, 'registration/order.html', {'form': form, 'username': get_user(request).username})


@login_required(login_url='/taxi/login')
def check_order(request):
    context = {
        'driver': "",
        'auto_brand': "",
        'auto_model': "",
        'number': ""
    }
    try:
        current_order = Orders.objects.get(client=Clients.objects.get(name=request.user), state=1)
        driver = Drivers.objects.get(driver_id=current_order.driver_id)
        print(driver.name)
        print(driver.vin.vin)
        print(driver)
        auto = driver.vin
        print(auto.model.model)
        context['driver'] = driver.name
        context['auto_model'] = auto.model.model
        context['number'] = auto.number
        context['auto_brand'] = auto.model.brand
    except Model.DoesNotExist:
        print("Something not found")

    return render(request, 'registration/check_order.html', context=context)


@login_required(login_url='/taxi/login')
def history(request):
    client = Clients.objects.get(name=request.user)
    print(client.name)
    o = Orders.objects.get(client=client, state=1)
    o.state = 0
    o.save()
    history_list = Orders.objects.filter(client=Clients.objects.get(name=request.user))
    print(type(history_list))
    context = {
        'history': history_list
    }
    return render(request, 'registration/history.html', context)


def calculate_sum():
    return random.randint(200, 3000)


def find_driver():
    return random.randint(1,10)