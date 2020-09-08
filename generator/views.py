from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here:
def home (request):#defining a function to "home" and returning a render, which is the Function
#to passback a template to the html response.
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz') #this variable with the funcion 'list' brings all the
    #characters (alphabetic)that will be used in the code below:
    length = int(request.GET.get('length', 12)) #password 'length' plus the function 'request.GET.get('length', 12)'
    # and the total size of 12 charaters as standard all as an int (número inteiro).
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('@#$%&*_=+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))#all this 'if request.GET.get('option')' is used to get the OPTIONS
        #of the charaters inside password request with the given possibilities presented in the 'home.html'.

    thepassword = '' #just added this variable because it is downthere in the dictionary...
    #now it is time to set the specs of thepassword of whatever we want it to be by setting a loop (laço):
    for x in range (length): #in a range (intervalo) where the "length" (tamanho) is "thepassword" plus and equal
    #to random.choice of the charaters (ou seja: a variável thepassword é igual a escolha aleatária de um caractere
    #da lista mais todos os caracteres, porque se ficar apenas 'thepassword = random.choice(charaters), vai aparecer
    #apenas um caractere).
        thepassword += random.choice(characters)




    return render(request, 'generator/password.html', {'password' : thepassword})
    # doing the same to show in our html "password.html", but adding a dictionary {'password'} and a variable
    #named 'thepassword'

def about(request):
    return render(request, 'generator/about.html')
