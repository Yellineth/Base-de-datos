# Maneja los datos de contacto de los clientes
import funciones 
cliente1 = {
        'id':'123',
        'nombre': 'Ivan', 
        'apellido': 'Calderon',
        'direccion': 'Suba',
        'correo': 'ivan@mail.com',
        'telefono': '3114694891'
}

cliente2 = {
        'id':'124',
        'nombre': 'Dario', 
        'apellido': 'Caceres',
        'direccion': 'Bucaramanga',
        'correo': 'dario@mail.com',
        'telefono': '3114698878'
}


clientes=[
    cliente1,
    cliente2
   
]

print('=========================================================')
funciones.mostrarLista(clientes)


opc=funciones.mostrarMenu()
while(opc!="3"):
    if opc == "1" :
        print("Vamos a agregar un nuevo cliente")
        nuevoCliente=funciones.agregarCliente()
        clientes.append(nuevoCliente)
        funciones.mostrarLista(clientes)
        opc=funciones.mostrarMenu()
    
    if opc=="2":
        print("Vamos a buscar un cliente")
        id=str(input(" ¿cual es el id a buscar?: "))
        cliente=funciones.buscarCliente(id,clientes)
        if cliente == "not found":
            print("No se encontro")
            opc=funciones.mostrarMenu()
        else:
            print("Elcliente encontrad fue:",cliente)


    if opc=="3":
        print("Has finalizados")