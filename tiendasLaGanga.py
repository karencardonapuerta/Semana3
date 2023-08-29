#Menu de Opciones
#1. registrar un producto a la bodega
#2. verificar los productos en la bodega
#3. buscar un producto en la bodega
#4. editar un producto en la bodega
#5. retirar un producto de la bodega
#6. salir


#producto: nombre, codigo,descripcion,foto,precio,cantidadBodega,fechaEntrada


opcion = 0

print ("Menu de Opciones")
print ("1. registrar un producto a la bodega")
print ("2. verificar los productos en la bodega")
print ("3. buscar un producto en la bodega")
print ("4. editar un producto en la bodega")
print ("5. retirar un producto de la bodega")
print ("6. salir")

productos = []


while (opcion != 6):
    
    
    producto= {}
    
    opcion= int (input("Digite la opcion deseada: "))
    
    if opcion == 1:
       
      
        producto ['nombre'] = input("Digite el nombre del producto: ")
        producto ['codigo'] = int(input("Digite el codigo del producto: "))
        producto ['descripcion'] = input("Digite la descripcion del producto: ")
        producto ['foto'] = input("Digite la url del producto: ")
        producto ['precio'] = float (input("Digite el precio del producto: "))
        producto ['cantidadBodega'] = int(input("Digite la cantidadBodega del producto: "))
        producto ['fechaEntrada'] = input("Digite la fechaEntrada del producto: ")
        productos.append(producto)

      
    elif opcion == 2:
        
        for productoSeleccionado in productos:
                print (f"codigo:  {productoSeleccionado['codigo']}")
                print (f"nombre:  {productoSeleccionado['nombre']}")
                print (f"descripcion:  {productoSeleccionado['descripcion']}")
                print (f"foto:  {productoSeleccionado['foto']}")
                print (f"precio:  {productoSeleccionado['precio']}")
                print (f"cantidadBodega:  {productoSeleccionado['cantidadBodega']}")
                print (f"fechaEntrada:  {productoSeleccionado['fechaEntrada']})\n")


             
    elif opcion == 3:
         pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    else:
        print("Opcion invalidad")














