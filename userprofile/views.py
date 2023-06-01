from django.contrib.auth import login  # login serve per loggare l'utente
from django.contrib.auth.forms import UserCreationForm
# UserCreationForm è un form che permette di creare un nuovo utente
from django.contrib.auth.models import User
from django.shortcuts import render, redirect  # redirect serve per reindirizzare l'utente verso un'altra pagina

from .models import Userprofile
def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, "vendor_detail.html", {"user": user})

def myaccount(request):
    return render(request, "myaccount.html")

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect("frontpage")  # reindirizza l'utente verso la pagina frontpage
        else:
            form = UserCreationForm()  # se il form non è valido, manda alla creazione

    return render(request, "signup.html", {
        "form": form
    })
