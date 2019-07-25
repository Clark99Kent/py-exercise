#CREIAMO UNA FUNZIONE/METODO PER LA STAMPA DI UNA LISTA .
def printList(list):
    if( len(list) == 0 ):
        print("La lista e' composta da ",  len(list), " elementi!")
    else:
        print(list[:])

#CREIAMO LA NOSTRA LISTA .
myList = []

#CONTROLLIAMO CHE LA NOSTRA LISTA SIA VUOTA .
printList(myList)

#AGGIUNGIAMO UN ELEMENTO .
print("""
PRIMO ELEMENTO INSERITO
""")
myList.append(30)
printList(myList)

#AGGIUNGIAMO UN SECONDO ELEMENTO .
print("""
SECONDO ELEMENTO INSERITO
""")
myList.append(10)
printList(myList)

#AGGIUNGIAMO UN ELEMENTO TRA I DUE INSERITI IN PRECEDENZA .
print("""
TERZO ELEMENTO INSERITO TRA I DUE PRECEDENTI
""")
myList.insert(1, 20)
printList(myList)

#VERIFICHIAMO SE UN ELEMENTO E' PRESENTE NELLA LISTA .
temp = int(input("Inserisci elemento da verificare: "))
if( temp in myList ):
    print("""
    L'elemento """, temp, """ e' presente nella lista 
    """)
else:
    print("""
    Elemento non presente!
    """)

#ELIMINIAMO UN ELEMENTO IN CODA .
print("""
ELIMINIAMO ELEMENTO IN CODA
""")
myList.pop()
printList(myList)

#ORDINIAMO LA LISTA DI ELEMENTI .
print("""
ORDINIAMO LA LISTA DI INTERI
""")
myList.sort()
printList(myList)

#PULIAMO LA LISTA .
print("""
PULIAMO LA LISTA
""")
myList.clear()
printList(myList)