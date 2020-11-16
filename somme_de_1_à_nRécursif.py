#!/usr/bin/python3
# coding : utf-8


def somme (n, maString):
  if (n == 1):
    print (maString+"1 soit ", end='')
    return 1
  if (n > 2):
    maString += str(n-1)+"+"
  return n + somme (n-1, maString) # Retourne toujours un réel et c’est impératif pour la récursivité.


try:
  n = int(input("Entrez le nombre dont on veut la somme avec tous ses précédents : "))
  print (str(somme (n, "La somme des chiffres de 1 à "+str(n)+" est "+str(n)+"+"))+".")
except:
  print ("Veuillez saisir un nombre. ")


----------------------------------------------------------------------- Résultat ------------------------------------------------------------------------------