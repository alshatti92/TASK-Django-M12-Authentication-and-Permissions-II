from atexit import register
from django.shortcuts import render, redirect
from users.forms import RegistrationForm
from django.contrib.auth import login

# Create your views here.


def register_user(req):
    form = RegistrationForm()
    if req.method == "POST":
        form = RegistrationForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            login(req, user)
            return redirect("home")

    context = {

        "form": form,
    }

    return render(req, "register.html", context)
