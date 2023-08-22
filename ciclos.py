
print("Departamento de confección")
print("1.Ingresar producto")
print("2..Mostrar inventario en fabrica")
print("0. SALIR")
opcion=100
listaProductos=[]
while opcion !=0:
    opcion=int(input("digita una opcion:"))
    if opcion==1:
       Producto=input("Digita el producto que ingresa a fabricación:")
       #Agregar un producto a la lista producto
       listaProductos.append(Producto)
    
    elif opcion==2:
        print("mostrando inventario:")
        print(listaProductos)
        
    elif opcion==0:
        print("Gracias, hasta pronto")
    else:  
        print("opcion inavalida")  
        print("opcion invalida..")
print("adios, Fin del programa")        