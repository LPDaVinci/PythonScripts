# Importiere das Numpy Package und deklariere es auf np
import numpy as np

# Importiere eine andere py Datei
import functions as f

#type
# str
# int
# float
# str(VALUE) # um den Datatype zu verändern auf einen String
# booolean (true, false)

# var
# varname = "text" or 'text'

# list
list1 = ['1', '2', '3']
# Printe Liste
print(list1)
# Indizierung einer liste Index startet bei 0 gibt die Zahl 2 aus
print(list1[1])

# bekomme die größe der Liste
print(len(list1))

#Überschreiben 3 mit 5
list1[2] = "5"
# Erweitere die Liste
list1.append('4')
#Lösche einen Eintrag aus der Liste
list1.remove('2')

print(list1)
# tuple
tupletest = (1,2,3)

# dictionary assoziatives array  for k,v in (bei lua)
dicttest = {1:"eins",2:"zwei",3:"drei"}

number = 1337

# + ist ein Operator um variablen und values zu addieren
name = "Test" + "LUL"

# print tuple
print(tupletest)

# print dict
print(dicttest)

# dict value vom key 1 
print(dicttest[1])

# print literals     
print(5)

# print variables
print(number)
print(name)

# Use numpy for random integer
print(np.random.randint(1,9))

# Lass die Funktion foo aus der Datei functions.py laufen
f.foo()    # prints "foo"
