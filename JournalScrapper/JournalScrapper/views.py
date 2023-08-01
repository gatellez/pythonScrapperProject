from django.shortcuts import render

from django.template import Template, Context

from django.http import HttpResponse


def index(request):
    doc_externo = open("C:/Users/telle/OneDrive/Documentos/proyecto/pythonScrapperProject/JournalScrapper/JournalScrapper/templates/index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    document = plt.render(ctx)
    return render(request, 'JournalScrapper/index.html',{})