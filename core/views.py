from django.shortcuts import render, HttpResponse
# Create your views here.
def hello(request,nome,idade):

    return HttpResponse(f'<h1><center>Hello Word, {nome} de {idade} anos!</center></h1>')


def soma(request,n1,n2):

    return HttpResponse(f'<h1><center>O resultado da soma de {n1} com {n2} é igual a {n1+n2}</center><h1>')


def multi(request,n1,n2):

    return HttpResponse(f'<h1><center>Multiplicação de {n1} e {n2} é igual a {n1*n2}</center></h1>')


def divisao(request,n1,n2):

    return HttpResponse(f"<h1><center>A divisão de {n1} e {n2} é igual a {n1 / n2:.2f}</center></h1>")


def sub(request,n1,n2):

    return HttpResponse(f'<h1><center>A subtração de {n1} e {n2} é igual a {n1-n2}</center></h1>')