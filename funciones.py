def mostrarLista(clientes):
    print('id   Nombre       Apellido           Direccion       Telefono')
    for cliente in clientes:
        print(cliente['id'],  cliente['nombre'],   cliente['apellido'],     cliente['direccion'],   cliente['correo'],  cliente['telefono'])

def mostrarMenu():
    print("1.Crear nuevo cliente")
    print("2.Buscar cliente")
    print("3.Salir")  
    opc=str(input(" Seleccione lo que desea hacer"))
    return opc  

def agregarCliente ():
    id=str(input(" ¿cual es si id? "))
    nombre=str(input(" ¿cual es el nombre del cliente? "))
    apellido=str(input(" ¿cual es el apellido del cliente? "))
    direccion=str(input(" ¿cual es la direccion del cliente? "))
    correo=str(input( "¿cual es el correo del cliente? " ))
    telefono=str(input(" ¿cual es el telefono del cliente? "))
    nuevoCliente={
        'id': id,
        'nombre': nombre, 
        'apellido': apellido,
        'direccion': direccion,
        'correo': correo,
        'telefono': telefono
    }
    return nuevoCliente

def buscarCliente (id,clientes):
    print("vamos a buscar cliente",id)
    for cliente in clientes:
        if cliente["id"]==id:
            return cliente
    return "not found"  
