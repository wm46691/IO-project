from django.shortcuts import render
from django.http import HttpResponse
from zadania.math_module.main import Calkowanie as c
from zadania.math_module.main import Bisekcja as bis
from zadania.math_module.main import Rozniczki as roz
from zadania.math_module.main import LU as lu
import os

from .forms import OdpForm
from .forms  import EmptyForm
# Create your views here.
def index2(request):
# Render the HTML template index.html
    return render(request, 'index.html')

def rozklad_lu(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OdpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user_odp_str = form.cleaned_data['odp']
            user_odp = user_odp_str.split(' ')
            X_list = request.session['X'].split(" ")
            is_correct = True
            for i in range(3):
                if X_list[i] != user_odp[i]:
                    is_correct = False
                    break
            if not is_correct:
                L = request.session['L']
                U = request.session['U']
                Y = request.session['Y']

    # if a GET (or any other method) we'll create a blank form
    else:
        user_odp_str = is_correct = L = U = None
        form = OdpForm()
        zadanie = lu()
        zadanie.Generate()
        zadanie.Calculate()
        A, b, X, Y, L, U = zadanie.Polecenie()
        request.session['A'] = A
        request.session['b'] = b
        request.session['X'] = X
        request.session['Y'] = Y
        request.session['L'] = L
        request.session['U'] = U
        #request.session['result'] = zadanie.GetResult()
    return render(request, 'lu.html', {'A' : request.session['A'], 'b' :request.session['b'], 'algo_odp' :request.session['X'], 'y' :request.session['Y'],'form': form, 'odp':user_odp_str, 'is_correct':is_correct,
    'L' : L, 'U' : U, 'Y':Y})

def calki(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OdpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user_odp = form.cleaned_data['odp']
            algo_odp = request.session['result']
            print(algo_odp)
            if round(float(user_odp), 3) == round(float(algo_odp), 3):
                is_correct = True
            else:
                is_correct = False
            gif_path = "my-gif.gif"

    # if a GET (or any other method) we'll create a blank form
    else:
        user_odp = algo_odp = is_correct = gif_path = None
        form = OdpForm()
        zadanie = c()
        zadanie.Generate()
        zadanie.Calculate()
        f, a, b, k = zadanie.Polecenie()
        request.session['f'] = str(f)
        request.session['a'] = a
        request.session['b'] = b
        request.session['k'] = k
        request.session['result'] = zadanie.GetResult()
        zadanie.Visualize()
    return render(request, 'calki.html', {'f' : request.session['f'], 'a':request.session['a'], 'b' :request.session['b'], 
    'k':request.session['k'], 'form': form, 'odp':user_odp, 'algo_odp':algo_odp, 'is_correct':is_correct, 'gif':gif_path})
    
def rownania_nieliniowe(request):
    odp = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OdpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user_odp = form.cleaned_data['odp']
            algo_odp = request.session['result']
            print(algo_odp)
            if round(float(user_odp), 3) == round(float(algo_odp), 3):
                is_correct = True
            else:
                is_correct = False
            gif_path = "my-gif.gif"
            #Pokaz wizualizacje
    # if a GET (or any other method) we'll create a blank form
    else:
        user_odp = algo_odp = is_correct = gif_path = None
        form = OdpForm()
        zadanie = bis()
        zadanie.Generate()
        zadanie.Calculate()
        f, a, b = zadanie.Polecenie()
        request.session['f'] = f
        request.session['a'] = a
        request.session['b'] = b
        request.session['result'] = zadanie.GetResult()
        zadanie.Visualize()
    return render(request, 'nieliniowe.html', {'f' : request.session['f'], 'a':request.session['a'], 'b' :request.session['b'], 'form': form, 'odp':user_odp, 'algo_odp':algo_odp, 'is_correct':is_correct, 'gif':gif_path})

def rozniczkowanie(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmptyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            odp = True

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmptyForm()
        zadanie = roz()
        zadanie.Generate()
        zadanie.Calculate()
        odp = False
        f, a, b, k, p = zadanie.Polecenie()
        request.session['f'] = f
        request.session['a'] = a
        request.session['b'] = b
        request.session['k'] = k
        request.session['p'] = p
        zadanie.Visualize()
    return render(request, 'rozniczkowanie.html', {'f' : request.session['f'], 'a':request.session['a'], 'b' :request.session['b'], 'krok':request.session['k'], 'p' :request.session['p'], 'form': form, 'odp':odp})

def simplex(request):
    return render(request, 'simplex.html')

def register2(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


#def logout(request):
#    return render(request, 'index.html')