#!/usr/bin/python3
import sys
import Pyro4 #el almacen ahora se obtiene de la red
from persona import Persona

sys.excepthook = Pyro4.util.excepthook #Esta instrucción permite obtener más datos 
                                       #por parte de pyro en caso de que ocurra una excepción 
                                       #en el objeto remoto

mialmacen = Pyro4.Proxy("PYRONAME:ejemplo.almacen") #construyendo objeto almacen
daniel = Persona("Daniel")
daniel.consulta(mialmacen)
