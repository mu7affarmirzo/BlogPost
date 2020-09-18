from django.shortcuts import render
from account.models import Account

def home_sreen_view(request):
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, "personal/home.html", context)