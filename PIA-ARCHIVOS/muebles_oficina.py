#Vamos a empezar a hacer el PIA

#Clases

class Comentario:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor

    def mostrar(self):
        return f"{self.autor}: {self.texto}"
    
    def __str__(self):
       return self.mostrar()

class Producto:
    def __init__(self, id_producto, descripcion, marca):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.marca = marca
        self.comentarios = []

    def agregar_comentario(self, comentario):
      self.comentarios.append(comentario)

    
    def mostrar(self):
        info = f"ID: {self.id_producto}\nDescripción: {self.descripcion}\nMarca: {self.marca}\nComentarios:\n"
        if self.comentarios:
            for c in self.comentarios:
                info += f" {c.mostrar()} \n"
        else:
            info += " (Sin comentarios)"
        return info
    
    def __str__(self):
         return self.mostrar()

def guardar_productos(productos, nombre_archivo):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p.id_producto}|{p.descripcion}|{p.marca}\n")
            for c in p.comentarios:
                archivo.write(f"*{c.autor}|{c.texto}\n")

def cargar_productos(nombre_archivo):
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            producto_actual = None
            for linea in archivo:
                linea = linea.strip()
                if linea.startswith("*"):
                    datos = linea[1:].split("|")
                    comentario = Comentario(datos[1], datos[0])
                    producto_actual.agregar_comentario(comentario)
                else:
                    datos = linea.split("|")
                    producto_actual = Producto(datos[0], datos[1], datos[2])
                    productos.append(producto_actual)
    except FileNotFoundError:
        pass
    return productos

def buscar_producto(productos, id_buscar):
    for p in productos:
        if p.id_producto == id_buscar:
            return p
    return None 

#Estructura

def menu():
    archivo = "productos.txt"
    productos = cargar_productos(archivo)

    while True:
        print("- Menu Muebles Oficina -")
        print("\n1. Agregar un producto\n2. Agregar comentarios\n3. Ver producto\n4. Ver productos\n5. Eliminar productos\n6. Modificar producto\n7. Salir")
        opcion = input("¿Que opcion que deseas trabajar?")
    
        if opcion == 1:
            id_p = input("Id del producto que deseas agregar: ")
            if buscar_producto(productos, id_p):
                print("El id ingresado ya está en uso.")
            else:
                desc = input("Descripción que gustas agregar: ")
                marca = input("Marca del producto: ")
                productos.append(Producto(id_p, desc, marca))
                guardar_productos(productos, archivo)

        if opcion == 2:
            id_p = input("Id del producto que deseas agregar el comentario: ")
            prod = buscar_producto(productos, id_p)
            if prod:
                autor = input("Nombre del autor: ")
                texto = input("Comentario: ")
                prod.agregar_comentario(Comentario(texto, autor))
                guardar_productos(productos, archivo)
            else:
                print("Id de producto no encontrado.")

        if opcion == 3:
            id_p = input("Id del producto que deseas ver: ")
            prod = buscar_producto(productos, id_p)
            if prod:
                print(prod)
            else:
                print("Id de producto no encontrado.")

        if opcion == 4:
            if productos:
                for p in productos:
                    print("\n" + str(p))
            else:
                print("No hay productos registrados.")

        if opcion == 5:
            id_p = input("ID del producto que deseas eliminar: ")
            encontrado = False
            for i in range(len(productos)):
                if productos[i].id_producto == id_p:
                    del productos[i]
                    encontrado = True
                    guardar_productos(productos, archivo)
                    print("Producto eliminado exitosamente.")
                    break
            if not encontrado:
                print("Id de producto no encontrado.")

        if opcion == 6:
            id_p = input("Id del producto que deseas modificar: ")
            prod = buscar_producto(productos, id_p)
            if prod:
                prod.descripcion = input("Ingrese la nueva descripción que guste agregar: ")
                prod.marca = input("Ingrese la nueva marca que guste agregar: ")
                guardar_productos(productos, archivo)
            else:
                print("Id de producto no encontrado.")

        if opcion == 7:
            print("¡Cerrando el programa, hasta luego <3!")
            break

        else:
            print("Opcion no valida, por favor ingrese otro valor.")

menu()