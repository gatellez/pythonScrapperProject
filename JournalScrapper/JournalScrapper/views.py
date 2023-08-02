from django.shortcuts import render

from django.http import HttpResponse
from . import scrapper


def index(request):
    return render(request, 'JournalScrapper/index.html',{'message':scrapper.getRepublica()})