from django.shortcuts import render
import random


def home(request):
    num = random.randint(0, 100)
    some_list = [
        num,
        random.randint(0, 10),
        random.randint(0, 1000)
    ]
    context ={
        "html_var": True,
        "num": num,
        "some_list": some_list
    }
    return render(request, "home.html", context)


def about(request):
    context ={}
    return render(request, "about.html", context)


def contact(request):
    context ={}
    return render(request, "contact.html", context)