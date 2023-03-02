#!/usr/bin/python3
import Pyro4
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Almacen(object):
    def __init__(self):
        self.inventario = {}
        with open("diccionario.txt") as file:
            for line in file:
                (key, val) = line.split("|")
                self.inventario[str(key)] = val

    def lista(self):
        return self.inventario

    def devuelve (self,nombre, articulo, value):
        self.inventario[articulo]
        print("{0} consultando {1}.".format(nombre, articulo))
        #print("Descripcion: {0}".format(value))
        

    def guarda(self,nombre,articulo, value):
        self.inventario[str(articulo)] = value
        print("{0} guardando {1}. con descripcion: {2}.".format(nombre, articulo, value))
    
def main():
    Pyro4.Daemon.serveSimple(
            {
                Almacen: "ejemplo.almacen"
            },
            host = "127.0.0.1",
            #host = "192.168.1.72",
            #host = servidor.uacm.edu.mx
            ns = True)

if __name__=="__main__":
    main()
    
