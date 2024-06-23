from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, ProfileUpdateForm
from .models import Profile
from myapp.models import Order
from django.http import HttpResponse
from django.contrib.auth import login  

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:index')
        else:
            print(form.errors)  
            # return HttpResponse("Перевірте правильність введених даних!")

    else:
        form = NewUserForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()
    return render(request, "users/profile.html")


def update(request):
    # Перевірка чи існує профіль
    profile = Profile.objects.get_or_create(user=request.user)[0]

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('users:profile')
        else:
            print(form.errors)
            return HttpResponse("Перевірте правильність введених даних!")

    else:
        form = ProfileUpdateForm(instance=profile)

    context = {'form': form}
    return render(request, 'users/update.html', context)


def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'users/user_orders.html', {'orders': orders})
