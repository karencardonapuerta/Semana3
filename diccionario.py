productoTerminadoUno = {
    'referencia':5070,
    'marca': "americanino",
    'descripcion':"chompa de acampar",
    'color': "naranja",
    'costoUnitario':100000,
    'Stock':True,
    'costoVenta':700000,
    'puntosDeVenta':['cc mayorca','terminal del norte','puerta del norte', 'centro de la moda']
}



productoTerminadoDos = {
    'referencia':5071,
    'marca': "americanino",
    'descripcion':"camiseta polo",
    'color': "azul oscuro",
    'costoUnitario':30000,
    'Stock':True,
    'costoVenta':150000,
    'puntosDeVenta':['cc mayorca','terminal del norte','puerta del norte', 'centro de la moda']
}

#Creando Una Lista De Diccionario

productos = [productoTerminadoUno,productoTerminadoDos]

#Recorriendo una lista con ciclo FOR
'''for contador in range(1,10,2):
    print(contador)'''

for producto in productos:
    for puntosDeVenta in producto["puntosDeVenta"]:
     print (puntosDeVenta)










