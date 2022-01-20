from django import forms

class SignUpForm(forms.Form):
    name =     forms.CharField(label='Ваше имя    ', max_length=20)
    lastname = forms.CharField(label='Ваша фамилия', max_length=20)
    password = forms.CharField(label='Пароль      ')
    phone =    forms.CharField(label='Телефон     ', max_length=11)
    card_number = forms.CharField(label='Номер карты', max_length=16)
    cvc = forms.IntegerField(label='CVC код')

class OrderForm(forms.Form):
    departure_longitude = forms.FloatField(label='Долгота точки отправления')
    departure_latitude = forms.FloatField(label='Широта точки отправления')
    arrival_longitude = forms.FloatField(label='Долгота точки назначения')
    arrival_latitude = forms.FloatField(label='Широта точки назначения')
