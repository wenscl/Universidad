from datetime import datetime


class NodoDatos(object): 

    def __init__(self):
        self.datos = ""


class NodoApuntador(object): 

    def __init__(self):
        self.apuntadores = [None for x in range(10)]


class NodoI(object): # tamanio es el tamanio que tienen los datos

    def __init__(self, tamanio, usuario, grupo, modo='0111101101'):
        self.tamanio = tamanio
        self.usuario = usuario
        self.grupo = grupo
        self.ctime = datetime.now()
        self.mtime = None
        self.atime = None
        # Permisos (el 1 al inicio indica que se trata de una carpeta)
        self.modo = modo
        # Apuntadores Directos
        self.datos = [None for x in range(10)]
        # Apuntadores Indirectos
        self.apuntadores = [None for x in range(3)]

    def chown(self, usuario):
        if '.' in usuario:
            usuario, grupo = usuario.split('.')
            self.chgrp(grupo)
        self.usuario = usuario

    def chgrp(self, grupo):
        self.grupo = grupo

    @property
    def is_dir(self):
        return self.modo.startswith('1') # si es 1 es un directorio


class FATItem(object): # listado de nodos y carpetas

    def __init__(self, nombre, id_nodoi):
        self.nombre = nombre
        self.id_nodoi = id_nodoi

    def __repr__(self):
        return "<FATItem '%s'-> %s" % (self.nombre, self.id_nodoi)


class FileSystem(object):

    def __init__(self, tamanio=10):
        self.fat = []
        self.nodos = []
        self.usuario = None
        self.grupo = None
        self.tamanio = tamanio  # tamanio maximo del filesystem. Por defecto esta en 10.
        self.actual_dir = "/"

    def excecute(self, acciones):
        archivo = open(acciones, "r")
        linea = archivo.readline()
        while linea != "":
            if len(linea.strip().split('|')) == 2:
                accion, nombre = linea.strip().split('|')
                self.HacerAccion(accion, nombre)
            else:
                if len(linea.strip().split('|')) > 2:
                    accion, nombre, dato = linea.strip().split('|')
                    self._HacerAccion(accion, nombre, dato)
            linea = archivo.readline()
        archivo.close()

    def HacerAccion(self, accion, nombre):
        if accion == "MD":
            if self.Existe(nombre) is not  None:
                print "Ya existe el directorio."
            else:
                varNodo = NodoI(self.tamanio,self.usuario,self.grupo)
                varFat = FATItem(self.actual_dir + nombre, id(varNodo))
                self.fat.append(varFat)
                self.nodos.append(varNodo)
                print "Se ha creado el directorio: " + self.actual_dir + nombre
                
        elif accion == "CD":
            if self.Existe(nombre) is not None:
                self.actual_dir = self.actual_dir + nombre + "/"
                print "El directorio actual es: " + self.actual_dir
            else:
                print "No existe el directorio."

        elif accion == "CF":
            if self.Existe(nombre) is None:
                varNodo = NodoI(self.tamanio, self.usuario, self.grupo)
                varFat = FATItem(self.actual_dir + nombre, id(varNodo))
                self.fat.append(varFat)
                self.nodos.append(varNodo)
                print "Se ha creado el archivo: " + self.actual_dir + nombre
            else:
                print "Ya existe un archivo con el mismo nombre."
            
        elif accion == "DF":
            DirFat = self.DirecFat(nombre)
            if DirFat is not None:
                for n in self.nodos:
                    if DirFat.id_nodoi == id(n):
                        if not ((self.usuario == n.usuario and n.modo[2] == "1") or (self.grupo == n.grupo and n.modo[5] == "1") or (n.modo[8] == "1")):
                            print "No se poseen los permisos necesarios para cambiar el usuario del archivo/directorio."
                        else:
                            self.nodos.remove(n)
                            self.fat.remove(DirFat)
                print "Se ha eliminado el archivo."
            else:
                print "No existe el archivo."

        elif accion == "RD":
            DirFat = self.DirecFat(nombre)
            if DirFat is not None:
                for n in self.nodos:
                    if DirFat.id_nodoi == id(n):
                        if not ((self.usuario == n.usuario and n.modo[2] == "1") or (self.grupo == n.grupo and n.modo[5] == "1") or (n.modo[8] == "1")):
                            print "No se poseen los permisos necesarios para cambiar el usuario del archivo/directorio."
                        else:
                            self.nodos.remove(n)
                            self.fat.remove(DirFat)
                print "Se ha eliminado el directorio."
            else:
                print "No existe el directorio"
            
        elif accion == "DU":
            self.usuario = nombre
            print "El usuario actual cambio a: " + self.usuario
            
        elif accion == "CG":
            self.grupo = nombre
            print "El grupo actual cambio a: " + self.grupo

    def FuncEscribir(self, lista, informacion):
        lista_aux = []
        for i in lista:
            if informacion != "":
                if i is None:
                    bloque = NodoDatos()
                    bloque.datos = informacion[:self.tamanio]
                    informacion = informacion[self.tamanio:]
                else:
                    bloque = i
                    if len(bloque.datos) < self.tamanio:
                        x = len(bloque.datos)
                        bloque.datos += informacion[:self.tamanio - len(bloque.datos)]
                        informacion = informacion[self.tamanio - x:]
                lista_aux.append(bloque)
            else:
                bloque = i
                lista_aux.append(bloque)
        return [lista_aux, informacion]

    def _HacerAccion(self, accion, nombre, dato):
        if accion == "WF":
                DirFat = self.DirecFat(nombre)
                if DirFat is not None:
                    varNodo = self.EncontrarNodoi(DirFat)
                    if not (varNodo is not None and not ((self.usuario == varNodo.usuario and varNodo.modo[2] == "1") or (self.grupo == varNodo.grupo and varNodo.modo[5] == "1") or (varNodo.modo[8] == "1"))):
                        while dato != "":
                            resultado = self.FuncEscribir(varNodo.datos, dato)
                            varNodo.datos = resultado[0]
                            dato = resultado[1]

                            if dato != "":
                                if varNodo.apuntadores[0] is None:
                                    varNodoapuntador = NodoApuntador()
                                else:
                                    varNodoapuntador = varNodo.apuntadores[0]
                                resultado = self.FuncEscribir(varNodoapuntador.apuntadores, dato)
                                varNodoapuntador.apuntadores = resultado[0]
                                dato = resultado[1]
                                varNodo.apuntadores[0] = varNodoapuntador

                                if dato != "":
                                    varNodoapuntador2 = varNodo.apuntadores[1]
                                    if varNodo.apuntadores[1] is None:
                                        varNodoapuntador2 = NodoApuntador()
                                    c = 0
                                    while (dato != "") and (c < 10):
                                        varNodoapuntador22 = varNodoapuntador2.apuntadores[c]
                                        if varNodoapuntador22 is None:
                                            varNodoapuntador22 = NodoApuntador()
                                        resultado = self.FuncEscribir(varNodoapuntador22.apuntadores, dato)
                                        varNodoapuntador22.apuntadores = resultado[0]
                                        dato = resultado[1]
                                        varNodoapuntador2.apuntadores[c] = varNodoapuntador22
                                        c += 1
                                    varNodo.apuntadores[1] = varNodoapuntador2

                                    if dato != "":
                                        varNodoapuntador3 = varNodo.apuntadores[2]
                                        if varNodo.apuntadores[2] is None:
                                            varNodoapuntador3 = NodoApuntador()
                                        c = 0
                                        while (dato != "") and (c < 10):
                                            varNodoapuntador33 = varNodoapuntador3.apuntadores[c]
                                            if varNodoapuntador33 is None:
                                                varNodoapuntador33 = NodoApuntador()
                                            d = 0
                                            while (dato != "") and (d < 10):
                                                varNodoapuntador333 = varNodoapuntador33.apuntadores[d]
                                                if varNodoapuntador333 is None:
                                                    varNodoapuntador333 = NodoApuntador()
                                                resultado = self.FuncEscribir(varNodoapuntador333.apuntadores, dato)
                                                varNodoapuntador333.apuntadores = resultado[0]
                                                dato = resultado[1]
                                                varNodoapuntador33.apuntadores[d] = varNodoapuntador333
                                                d += 1
                                            varNodoapuntador3.apuntadores[c] = varNodoapuntador33
                                            c += 1
                                        varNodo.apuntadores[2] = varNodoapuntador3

                                        if dato != "":
                                            print "El texto a escribir excedia la capacidad del archivo. No se ha guardado: " + dato
                            break
                        varNodo.mtime = datetime.now()
                        print "El archivo '" + self.actual_dir + nombre + "' ha sido escrito con exito."
                    else:
                        print "No se poseen los permisos necesarios para cambiar el usuario del archivo/directorio."
        elif accion == "AG":
            DirFat = self.DirecFat(nombre)
            if DirFat is not None:
                for n in self.nodos:
                    if id(n) == DirFat.id_nodoi:
                        if not ((self.usuario == n.usuario and n.modo[2] == "1") or (self.grupo == n.grupo and n.modo[5] == "1") or (n.modo[8] == "1")):
                            print "No se poseen los permisos necesarios para cambiar el usuario del archivo/directorio."
                        else:
                            n.grupo = dato
                            n.mtime = datetime.now()
            else:
                print "No existe el archivo/directorio especificado"

    def Existe(self, nombre):
        for e in self.fat:
            if e.nombre == self.actual_dir + nombre:
                return e.nombre
        return None

    def DirecFat(self, nombre):
        for e in self.fat:
            if e.nombre == self.actual_dir + nombre:
                return e
        return None
    
    def EncontrarNodoi(self, directorio):
        for f in self.fat:
            if f.nombre == directorio.nombre:
                for n in self.nodos:
                    if id(n) == f.id_nodoi:
                        return n
        return None

    def read_file(self, archivo):
        nodobuscar = None
        for f in self.fat:
            if f.nombre == archivo:
                for n in self.nodos:
                    if id(n) == f.id_nodoi:
                        nodobuscar = n
        if nodobuscar is None:
            return "El archivo no existe."
        else:
            if not ((self.usuario == nodobuscar.usuario and nodobuscar.modo[1] == "1") or (self.grupo == nodobuscar.grupo and nodobuscar.modo[4] == "1") or (nodobuscar.modo[7] == "1")):
                return "No se poseen los permisos necesarios para leer el archivo."
            informacion = ""
            for dat in nodobuscar.datos:
                if dat is not None:
                    informacion += dat.datos
                else:
                    return "La informacion del archivo '" + archivo + "' es:" + informacion

            if nodobuscar.apuntadores[0] is not None:
                l1 = nodobuscar.apuntadores[0]
                for dat in l1.apuntadores:
                    if dat is not None:
                        informacion += dat.datos
                    else:
                        return "La informacion del archivo '" + archivo + "' es:" + informacion
            else:
                return "La informacion del archivo '" + archivo + "' es:" + informacion

            if nodobuscar.apuntadores[1] is not None:
                l2 = nodobuscar.apuntadores[1]
                d = 0
                l22 = l2.apuntadores[d]
                while l22 is not None and d < 10:
                    l22 = l2.apuntadores[d]
                    if l22 is None:
                        break
                    for dat in l22.apuntadores:
                        if dat is not None:
                            informacion += dat.datos
                        else:
                            return "La informacion del archivo '" + archivo + "' es:" + informacion
                    d += 1
            else:
                return "La informacion del archivo '" + archivo + "' es:" + informacion

            if nodobuscar.apuntadores[2] is not None:
                l3 = nodobuscar.apuntadores[2]
                d = 0
                l33 = l3.apuntadores[d]
                while l33 is not None and d < 10:
                    l33 = l3.apuntadores[d]
                    if l33 is None:
                        break
                    e = 0
                    l333 = l33.apuntadores[e]
                    while l333 is not None and e < 10:
                        l333 = l33.apuntadores[d]
                        if l333 is None:
                            break
                        for dat in l333.apuntadores:
                            if dat is not None:
                                informacion += dat.datos
                            else:
                                return "La informacion del archivo '" + archivo + "' es:" + informacion
                        e += 1
                    d += 1
                return "La informacion del archivo '" + archivo + "' es:" + informacion
            else:
                return "La informacion del archivo '" + archivo + "' es:" + informacion



    def get_file_metadata(self, archivo):
        nodobuscar = None
        for e in self.fat:
            if e.nombre == archivo:
                for n in self.nodos:
                    if id(n) == e.id_nodoi:
                        nodobuscar = n
        if nodobuscar is None:
            print "El archivo no existe."
        else:
            metadatos = ""
            metadatos += "Metadatos del archivo '" + archivo + "':" + "\n"
            metadatos += "    - Usuario: " + nodobuscar.usuario + "\n"
            metadatos += "    - Grupo: " + nodobuscar.grupo + "\n"
            metadatos += "    - Fecha de Creacion: " + str(nodobuscar.ctime) + "\n"
            metadatos += "    - Fecha de Modificacion: " + str(nodobuscar.mtime) + "\n"
            metadatos += "    - Fecha de Acceso: " + str(nodobuscar.atime) + "\n"
            metadatos += "    - Modo: " + nodobuscar.modo + "\n"
            return metadatos
       
    def get_tree(self, directorio):
        raise NotImplementedError


if __name__ == '__main__':
    acciones = 'acciones.txt'

    fs = FileSystem()
    fs.usuario = 'usuario_1'
    fs.grupo = 'grupo_1'
    print fs.actual_dir
    fs.excecute(acciones) 

    print fs.fat
    print fs.actual_dir 
    print fs.read_file('/DatosAC1/Datos.txt')
    print fs.get_file_metadata('/DatosAC1/Datos.txt')
    # print fs.get_tree('/')
