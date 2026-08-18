from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, welcome to Django!")
def hi(display):
    return HttpResponse("HELLO, HOW ARE YOU ? ")
def bye(display):
    return HttpResponse("HOPE YOU ARE FINE ! ")


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

