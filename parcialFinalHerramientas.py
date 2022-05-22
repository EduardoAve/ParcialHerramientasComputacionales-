from ast import If
from bdb import effective
from multiprocessing.connection import wait
import random
print("\nBienvenidos al restaurante\n")
seguir=1
costoFinal = 0
nombre=str(input("\nPorfavor ingrese su nombre: "))

try:
    
    tipo = int(input("\nporfavor ingrese el tipo de cliente que desea realizar la compra (1)Estudiante, (2)Profesor  : "))
    
except:
    
    print("\ningrese la informacion de la forma indicada en el tipo de cliente, vuelva a intentarlo.\n")
    quit();
    
try:
    
    cedula = float(input("\nporfavor ingrese su numero de identificacion(C.C) solo numeros, sin puntos : "))
    
except:
    print("\ningrese la informacion de la forma indicada en la cedula, vuelva a intentarlo.\n")
    quit();
    
try:
    
    while seguir == 1:
        
        try:
            
            if tipo == 1:
                
                tipoEstudiante = int(input("\n(1)Estudiante becado, (2)Estudiante sin beca: "))
                
        except:
            
            print("\nSe ingreso un tipo de estudiante no valido, se tomara como estudiante no becado\n")
            tipoEstudiante=2
            
        producto = int(input("\n(1)Almuerzo ejecutivo\n(2)Almuerzo a la carta\n(3)Bebidas\n: "))
        
        try:
            
            if producto == 3:
                
                bebida = int(input("\n(31)Coca Cola\n(32)Pepsi\n(33)Manzana postobon\n: "))
                
                try:
                    
                    if bebida == 31:
                        precio = 2500
                        producto = bebida
                    elif bebida == 32:
                        precio = 2500
                        producto = bebida
                    elif bebida == 33:
                        precio = 2000
                        producto = bebida
                    else:
                        print("\nIngrese un valor valido\n")
                        
                except:
                    print("\nno se ha encontrado el tipo de bebida buscado\n")
                    precio=0
                    
            elif producto == 2:
                precio = 20000
            elif producto == 1:
                precio = 11000
            else:
                print("\ningrese un valor valido\n")
                
        except:
            
            print("\nSe ingreso un valor no valido al ecoger el tipo de producto\n")
            precio=0
        cantidad = int(input("\n¿Que cantidad de unidades del producto desea comprar?: "))
        
        try:
            
            if tipo == 1:
                if tipoEstudiante == 1:
                    costo=precio * 0.5 * cantidad
                elif tipoEstudiante == 2:
                    costo=precio * 0.7 * cantidad
                else:
                    print("\nha habido un error en el tipo de estudiante\n")
            elif tipo == 2:
                costo = precio*0.8 * cantidad
            else:
                print("\nha habido un error en e tipo de cliente\n")
                
        except:
            cantidad=1
            print("Cantidad ingresada no valida, se toma la cantidad de unidades como 1")
            
        if tipo==1:
            print("\n el estudiante ",nombre," con cedula numero ",cedula," debe pagar ",costo,"$")
            print(" por el producto codigo ",producto,"\n")
        elif tipo==2:
            print("\n el profesor ",nombre," con cedula numero ",cedula," debe pagar ",costo,"$")
            print(" por",cantidad, " unidades del producto codigo ",producto,"\n")
        else:
            print("\nha ocurrido un error\n")
            
        try:
            seguir = int(input("\n¿Desea agregar otro producto a su factura?(1)Si,(2)No :  \n"))  
        except:
            seguir = 2
            print("\nDato incorrecto, se tomara como no agregar otro producto\n")
            
        
        
    costoFinal = costoFinal + costo
    if tipo == 1:
        print("\n el estudiante ",nombre," con cedula numero ",cedula," debe pagar un total de ",costoFinal,"$\n")
    elif tipo == 2:
        print("\n el profesor ",nombre," con cedula numero ",cedula," debe pagar un total de ",costoFinal,"$\n")
    
except:
    
    quit();
