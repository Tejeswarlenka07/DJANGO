from django.shortcuts import render, redirect
from .models import User

# INSERT FORM
def add_user(request):
    return render(request, 'add.html')


# INSERT SAVE
def save_user(request):
    if request.method == 'POST':
        User.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            country=request.POST.get('country')
        )
        return redirect('view')


# VIEW
def view_users(request):
    data = User.objects.all()
    return render(request, 'view.html', {'data': data})


# DELETE
def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect('view')


# EDIT FORM
def edit_user(request, id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})


# UPDATE SAVE
def update_user(request, id):
    user = User.objects.get(id=id)
    user.username = request.POST.get('username')
    user.email = request.POST.get('email')
    user.country = request.POST.get('country')
    user.save()
    return redirect('view')