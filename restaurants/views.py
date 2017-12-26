from django.shortcuts import render
import random


def home(request):
    num = random.randint(0, 100)
    return render(request, "base.html", {"html_var": "context_variable", "num": num})
