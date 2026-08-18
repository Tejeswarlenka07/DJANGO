from django.shortcuts import render
from .models import Registration

def index(request):
    return render(request, 'index.html')


def register_form(request):
    return render(request, 'register.html')


def register_result(request):
    if request.method == "POST":
        username = request.POST.get('username')
        country = request.POST.get('country')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        hobbies_list = request.POST.getlist('hobbies')   
        hobbies = ", ".join(hobbies_list)                

        reg = Registration(
            username=username,
            country=country,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies
        )
        reg.save()

        return render(request, 'register_result.html', {
            'username': username,
            'country': country,
            'email': email,
            'password': password,
            'gender': gender,
            'hobbies': hobbies_list
        })