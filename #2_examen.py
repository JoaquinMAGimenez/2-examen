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
JEDIS =[        
            {'nombre':'qui-gon jin','altura':'1.93','peso': '75'},
            {'nombre':'yoda','altura':'0.45','peso': '15'},
            { 'nombre':'asoka','altura':'1.45','peso': '55'},
            {'nombre':'mandalorian', 'altura': 1.85,'peso': 76},
            {'nombre':'mace windu', 'altura': 1.82,'peso': 74}
            {'nombre':'plo koon', 'altura': 1.74,'peso': 72},
            {'nombre':'yaddle', 'altura': 1.79,'peso': 71},
            {'nombre':'adi gallia', 'altura': 1.85,'peso': 68},
            {'nombre':'kit fisto', 'altura': 1.88,'peso': 87},
            {'nombre':'luminara unduli', 'altura': 1.93,'peso': 77},
            {'nombre':'sifo-dyas', 'altura': 1.99,'peso': 97},
            {'nombre':'bultar swan', 'altura': 1.84,'peso': 99},
            {'nombre':'agen kolar', 'altura': 1.77,'peso': 107},
            {'nombre':'stass allie', 'altura': 1.73,'peso': 100},
            {'nombre':'asajj ventress', 'altura': 1.37,'peso': 84},
            {'nombre':'nahdar vebb', 'altura': 0.58,'peso': 66},
            {'nombre':'bolla ropal', 'altura': 1.85,'peso': 62},
            {'nombre':'leia organa', 'altura': 1.55,'peso': 65},
            {'nombre':'grogu', 'altura': 1.99,'peso': 120},
            {'nombre':'obi-wan kenobi', 'altura': 1.64,'peso': 57},   
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
print('la altura de Grogu es:', nodo_buscado2)