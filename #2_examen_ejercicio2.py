#2_examen_ejercicio2.py

'''
2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver 
las siguientes tareas:
a. cada vértice debe almacenar el nombre de un personaje, las aristas representan 
la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren,
 Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.'''

from grafo import Grafo

g=Grafo()

#a y d
#vertices
g.insertar_vertice('C3PO')
g.insertar_vertice('Yoda')
g.insertar_vertice('princesa Leila')
g.insertar_vertice('Luke Skywalker')
g.insertar_vertice(' Darth Vader')
g.insertar_vertice('Boba Fett')
g.insertar_vertice('Rey')
g.insertar_vertice('Kylo Ren')
g.insertar_vertice('Chewbacca')
g.insertar_vertice('Han Solo')
g.insertar_vertice('R2-D2')
g.insertar_vertice('Obi-Wan Kenobi')
g.insertar_vertice('BB-8')


#aristas
g.insertar_arista('C3PO','Yoda', 1)
g.insertar_arista('C3PO','princesa Leila', 1)
g.insertar_arista('C3PO','Luke Skywalker', 8)
g.insertar_arista('C3PO','Darth Vader', 0)
g.insertar_arista('C3PO','Boba Fett', 0)
g.insertar_arista('C3PO','Rey', 1)
g.insertar_arista('C3PO','Kylo Ren', 10)
g.insertar_arista('C3PO','Chewbacca', 1)
g.insertar_arista('C3PO','Han Solo', 1)
g.insertar_arista('C3PO','R2-D2', 2)
g.insertar_arista('C3PO','Obi-Wan Kenobi', 4)
g.insertar_arista('C3PO','BB-8', 0)

g.insertar_arista('Yoda','C3PO', 1)
g.insertar_arista('Yoda','princesa Leila', 0)
g.insertar_arista('Yoda','Luke Skywalker', 1)
g.insertar_arista('Yoda','Darth Vader', 0)
g.insertar_arista('Yoda','Boba Fett', 0)
g.insertar_arista('Yoda','Rey', 1)
g.insertar_arista('Yoda','Kylo Ren', 10)
g.insertar_arista('Yoda','Chewbacca', 1)
g.insertar_arista('Yoda','Han Solo', 1)
g.insertar_arista('Yoda','R2-D2', 2)
g.insertar_arista('Yoda','Obi-Wan Kenobi', 4)
g.insertar_arista('Yoda','BB-8', 0)

g.insertar_arista('princesa Leila','Yoda', 0)
g.insertar_arista('princesa Leila','C3PO', 1)
g.insertar_arista('princesa Leila','Luke Skywalker', 1)
g.insertar_arista('princesa Leila','Darth Vader', 0)
g.insertar_arista('princesa Leila','Boba Fett', 0)
g.insertar_arista('princesa Leila','Rey', 1)
g.insertar_arista('princesa Leila','Kylo Ren', 10)
g.insertar_arista('princesa Leila','Chewbacca', 1)
g.insertar_arista('princesa Leila','Han Solo', 1)
g.insertar_arista('princesa Leila','R2-D2', 2)
g.insertar_arista('princesa Leila','Obi-Wan Kenobi', 4)
g.insertar_arista('princesa Leila','BB-8', 0)

g.insertar_arista('Luke Skywalker','Yoda', 1)
g.insertar_arista('Luke Skywalker','princesa Leila', 1)
g.insertar_arista('Luke Skywalker','C3PO', 8)
g.insertar_arista('Luke Skywalker','Darth Vader', 0)
g.insertar_arista('Luke Skywalker','Boba Fett', 0)
g.insertar_arista('Luke Skywalker','Rey', 1)
g.insertar_arista('Luke Skywalker','Kylo Ren', 10)
g.insertar_arista('Luke Skywalker','Chewbacca', 1)
g.insertar_arista('Luke Skywalker','Han Solo', 1)
g.insertar_arista('Luke Skywalker','R2-D2', 2)
g.insertar_arista('Luke Skywalker','Obi-Wan Kenobi', 4)
g.insertar_arista('Luke Skywalker','BB-8', 0)

g.insertar_arista('Darth Vader','Yoda', 0)
g.insertar_arista('Darth Vader','princesa Leila', 0)
g.insertar_arista('Darth Vader','Luke Skywalker', 0)
g.insertar_arista('Darth Vader','C3PO', 0)
g.insertar_arista('Darth Vader','Boba Fett', 0)
g.insertar_arista('Darth Vader','Rey', 1)
g.insertar_arista('Darth Vader','Kylo Ren', 10)
g.insertar_arista('Darth Vader','Chewbacca', 1)
g.insertar_arista('Darth Vader','Han Solo', 1)
g.insertar_arista('Darth Vader','R2-D2', 2)
g.insertar_arista('Darth Vader','Obi-Wan Kenobi', 4)
g.insertar_arista('Darth Vader','BB-8', 1)

g.insertar_arista('Boba Fett','Yoda', 0)
g.insertar_arista('Boba Fett','princesa Leila', 0)
g.insertar_arista('Boba Fett','Luke Skywalker', 0)
g.insertar_arista('Boba Fett','C3PO', 0)
g.insertar_arista('Boba Fett','Darth Vader', 0)
g.insertar_arista('Boba Fett','Rey', 1)
g.insertar_arista('Boba Fett','Kylo Ren', 10)
g.insertar_arista('Boba Fett','Chewbacca', 1)
g.insertar_arista('Boba Fett','Han Solo', 1)
g.insertar_arista('Boba Fett','R2-D2', 2)
g.insertar_arista('Boba Fett','Obi-Wan Kenobi', 4)
g.insertar_arista('Boba Fett','BB-8', 10)

g.insertar_arista('Rey','Yoda', 1)
g.insertar_arista('Rey','princesa Leila', 1)
g.insertar_arista('Rey','Luke Skywalker', 1)
g.insertar_arista('Rey','C3PO', 1)
g.insertar_arista('Rey','Darth Vader', 1)
g.insertar_arista('Rey','Boba Fett', 1)
g.insertar_arista('Rey','Kylo Ren', 10)
g.insertar_arista('Rey','Chewbacca', 1)
g.insertar_arista('Rey','Han Solo', 1)
g.insertar_arista('Rey','R2-D2', 2)
g.insertar_arista('Rey','Obi-Wan Kenobi', 4)
g.insertar_arista('Rey','BB-8', 10)

g.insertar_arista('Kylo Ren','Yoda', 10)
g.insertar_arista('Kylo Ren','princesa Leila', 10)
g.insertar_arista('Kylo Ren','Luke Skywalker', 10)
g.insertar_arista('Kylo Ren','C3PO', 10)
g.insertar_arista('Kylo Ren','Darth Vader', 10)
g.insertar_arista('Kylo Ren','Boba Fett', 10)
g.insertar_arista('Kylo Ren','rey', 10)
g.insertar_arista('Kylo Ren','Chewbacca', 1)
g.insertar_arista('Kylo Ren','Han Solo', 1)
g.insertar_arista('Kylo Ren','R2-D2', 2)
g.insertar_arista('Kylo Ren','Obi-Wan Kenobi', 4)
g.insertar_arista('Kylo Ren','BB-8', 1)


g.insertar_arista('Han Solo','Yoda', 1)
g.insertar_arista('Han Solo','princesa Leila', 1)
g.insertar_arista('Han Solo','Luke Skywalker', 1)
g.insertar_arista('Han Solo','C3PO', 1)
g.insertar_arista('Han Solo','Darth Vader', 1)
g.insertar_arista('Han Solo','Boba Fett', 1)
g.insertar_arista('Han Solo','rey', 1)
g.insertar_arista('Han Solo','Chewbacca', 1)
g.insertar_arista('Han Solo','Kylo Ren', 1)
g.insertar_arista('Han Solo','R2-D2', 2)
g.insertar_arista('Han Solo','Obi-Wan Kenobi', 4)
g.insertar_arista('Han Solo','BB-8', 1)

g.insertar_arista('Chewbacca','Yoda', 1)
g.insertar_arista('Chewbacca','princesa Leila', 1)
g.insertar_arista('Chewbacca','Luke Skywalker', 1)
g.insertar_arista('Chewbacca','C3PO', 0)
g.insertar_arista('Chewbacca','Darth Vader', 1)
g.insertar_arista('Chewbacca','Boba Fett', 1)
g.insertar_arista('Chewbacca','rey', 1)
g.insertar_arista('Chewbacca','Kylo Ren', 1)
g.insertar_arista('Chewbacca','Han Solo', 1)
g.insertar_arista('Chewbacca','R2-D2', 2)
g.insertar_arista('Chewbacca','Obi-Wan Kenobi', 4)
g.insertar_arista('Chewbacca','BB-8', 1)

g.insertar_arista('R2-D2','Yoda', 2)
g.insertar_arista('R2-D2','princesa Leila', 2)
g.insertar_arista('R2-D2','Luke Skywalker',2)
g.insertar_arista('R2-D2','C3PO', 2)
g.insertar_arista('R2-D2','Darth Vader', 2)
g.insertar_arista('R2-D2','Boba Fett', 2)
g.insertar_arista('R2-D2','rey', 2)
g.insertar_arista('R2-D2','Chewbacca', 2)
g.insertar_arista('R2-D2','Kylo Ren', 2)
g.insertar_arista('R2-D2','Han Solo', 2)
g.insertar_arista('R2-D2','Obi-Wan Kenobi', 4)
g.insertar_arista('R2-D2','BB-8', 2)

g.insertar_arista('Obi-Wan Kenobi','Yoda', 4)
g.insertar_arista('Obi-Wan Kenobi','princesa Leila',4)
g.insertar_arista('Obi-Wan Kenobi','Luke Skywalker', 4)
g.insertar_arista('Obi-Wan Kenobi','C3PO', 4)
g.insertar_arista('Obi-Wan Kenobi','Darth Vader', 4)
g.insertar_arista('Obi-Wan Kenobi','Boba Fett', 4)
g.insertar_arista('Obi-Wan Kenobi','rey', 4)
g.insertar_arista('Obi-Wan Kenobi','Chewbacca', 4)
g.insertar_arista('Obi-Wan Kenobi','Han Solo', 1)
g.insertar_arista('Obi-Wan Kenobi','R2-D2', 4)
g.insertar_arista('Obi-Wan Kenobi','Kylo Ren', 4)
g.insertar_arista('Obi-Wan Kenobi','BB-8', 1)

g.insertar_arista('BB-8','Yoda', 0)
g.insertar_arista('BB-8','princesa Leila', 0)
g.insertar_arista('BB-8','Luke Skywalker', 0)
g.insertar_arista('BB-8','C3PO', 0)
g.insertar_arista('BB-8','Darth Vader', 1)
g.insertar_arista('BB-8','Boba Fett', 10)
g.insertar_arista('BB-8','rey', 10)
g.insertar_arista('BB-8','Chewbacca', 1)
g.insertar_arista('BB-8','Han Solo', 1)
g.insertar_arista('BB-8','R2-D2', 2)
g.insertar_arista('BB-8','Obi-Wan Kenobi', 1)
g.insertar_arista('BB-8','Kylo Ren', 1)

g.barrido_vertice()
print()

#b
arbol_min = g.kruskal()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    print(nodo)
    nodo = nodo.split(';')

    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el peso total es {peso_total}")
print ('arbol minimo de C3PO:', arbol_min('C3po'))
print ('arbol minimo de Yoda:', arbol_min('Yoda'))
print ('arbol minimo de princesa Leila:', arbol_min('Cprincesa Leila'))

#c
aux=0
while aux is not None in g:
    if g.adyacentes('peso') >=2:
        print(g.adyacentes())
#e
    a=0
    while  aux is not None in g:  
        if g.adyacentes('peso')>a:
            personaje_con_mayor_relaciones = g.adyacentes()
            print('el personaje con mas relaciones es:',personaje_con_mayor_relaciones)
        else:
            a=g.adyacentes('peso')


