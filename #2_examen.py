#2_examen.py
#ejercicio1
'''1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes de la saga 
de Star Wars, de los cuales se sabe su nombre, altura y peso. Además deberá contemplar los siguientes
 requerimientos (debe cargar al menos 20 personajes):
a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
e. mostrar un listado por nivel de los personajes del árbol;
f. determinar si Grogu esta en el árbol y responder lo siguiente:

    mostrar toda su información;
    en que tipo de nodo esta (hoja, intermedio o raíz);
    que altura tiene el nodo dentro del árbol.'''

import modulo_arbol

arbol_jedi = modulo_arbol.nodoArbol()
JEDIS = [       
        {'nombre':'qui-gon jin','altura':'1.93','peso': '75'},
        {'nombre':'yoda','altura':'0.45','peso': '15'},
        { 'nombre':'asoka','altura':'1.45','peso': '55'},
] 



for j in JEDIS:
     modulo_arbol.insertar_nodo(arbol_jedi,j['nombre'],{ 'altura':j['altura'] , 'peso':j['peso']})

#a
print('cargue un nuevo jedai')
nombre = input()
arbol_jedi.remplazar(nombre)
print('ingrese su altura')
altura = input()
arbol_jedi.remplazar(altura)
print ('ingrese su peso')
peso = input()
arbol_jedi.remplazar(peso)
#b
if( j['nombre'] == 'yoda') or (j['nombre']=='Mandalorian') or (j['nombre']=='Luke Skywalker') :
    print(arbol_jedi.busqueda(arbol_jedi,'info'))
#c

if(j['altura'] < '0.9'):
    print('jedis que miden menos de 0.9:')
    print(arbol_jedi.busqueda(arbol_jedi,'nombre'))

#d
if('peso' >'75'):
    print("jedis que pesan mas de 75:")
    print(arbol_jedi.busqueda(arbol_jedi,'peso'))
#e
por_nivel = modulo_arbol.por_nivel(arbol_jedi)
print('el orden del arbol por nivel es',por_nivel)
#f
if( j['nombre'] == 'Grogu'):
  nodo_buscado = modulo_arbol.busqueda(arbol_jedi, "Grogu")
  nodo_buscado2 = modulo_arbol.busqueda(arbol_jedi, altura)
print('Informacion de Grogu: ', nodo_buscado)
