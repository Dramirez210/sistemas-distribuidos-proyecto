from Pyro4 import socketutil

class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def consulta(self, almacen):
        print("Bienvenido/a al almacen {0}.\n".format(self.nombre))
        self.peticion(almacen)
        print("Gracias!")
        
    def deposita(self, almacen, articulo):
        if articulo:
            descripcion = input("Escriba una descripcion del articulo (o vacio):").strip()
            almacen.guarda(self.nombre, articulo, descripcion)

    def peticion(self, almacen):
        print("El almacen contiene:", [x for x in almacen.lista().keys()])
        articulo = input("\nEscriba que desea consultar (o vacio): ").strip()
        if articulo:
            value = almacen.lista().get(articulo)
            try: 
               almacen.devuelve(self.nombre, articulo, value)
               print("Abstract: {0}".format(value))
            except:
               print("No fue posible procesar su peticion: '{0}'. Si considera que es un error comuniquese al 01800-554544".format(articulo))
               addItem = input("o ¿Desea agregar el articulo {0} ('SI' o vacio)? ".format(articulo))
               if addItem.lower() == 'si':
                   self.deposita(almacen, articulo)
            #return value
             
