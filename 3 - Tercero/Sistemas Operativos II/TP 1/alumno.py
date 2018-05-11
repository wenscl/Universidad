import pickle
from catedra import Bloque, Algoritmo, Memoria, SOException


class PrimerAjuste(Algoritmo):

    def __init__(self):
        super(PrimerAjuste, self).__init__("PrimerAjuste")

    def colocar(self, dato):
        if (dato.tamanio <= self.memoria.longitud):
            if len(self.memoria.datos) == 0:
                dato.inicio = 0 #Primer bloque colocado al principio
            else:
                #Ordenar los bloques en memoria segun su tiempo de inicio
                self.memoria.datos.sort(key = lambda x: x.inicio)
                
                fin = 0
                for b in self.memoria.datos:
                    if b.id_proceso != None:
                        #Busca un lugar vacio y si puede, ubica al bloque
                        if dato.tamanio <= (b.inicio - fin): 
                            if dato.inicio == None:
                                dato.inicio = fin
                                break
                        else:
                            fin = b.tamanio + b.inicio
                #Si no encuentra lugar, coloca al bloque en el final
                if (dato.inicio == None) and ((self.memoria.longitud - fin) >= dato.tamanio):
                    dato.inicio = fin 


class MejorAjuste(Algoritmo):

    def __init__(self):
        super(MejorAjuste, self).__init__("MejorAjuste")

    def colocar(self, dato):
        if (dato.tamanio <= self.memoria.longitud):
            if len(self.memoria.datos) == 0:
                dato.inicio = 0
            else:
                self.memoria.datos.sort(key=lambda x: x.inicio)
                
                mejor = None
                fin = 0
                for b in self.memoria.datos:
                    if b.id_proceso != None:
                        #Busca el mejor espacio para ubicar al bloque
                        if dato.tamanio <= (b.inicio - fin):
                            if (mejor == None) or (mejor > (b.inicio - fin)):
                                mejor = (b.inicio - fin)
                                inicio = fin   
                        fin = b.tamanio + b.inicio
                if (self.memoria.longitud - fin) >= dato.tamanio:      
                    if mejor == None:
                        dato.inicio = fin
                    else:
                        if mejor <= (self.memoria.longitud - fin):
                            dato.inicio = inicio #Si encontro un lugar, coloca al bloque
                        else:
                            dato.inicio = fin #Si no encuentra, coloca al bloque en el final


class PeorAjuste(Algoritmo):

    def __init__(self):
        super(PeorAjuste, self).__init__("PeorAjuste")

    def colocar(self, dato):
        if (dato.tamanio <= self.memoria.longitud):
            if len(self.memoria.datos) == 0:
                dato.inicio = 0
            else:
                self.memoria.datos.sort(key=lambda x: x.inicio)
                
                peor = None
                fin = 0
                inicio = None
                for b in self.memoria.datos:
                    if b.id_proceso != None:
                        #Busca el mejor espacio para ubicar al bloque
                        if dato.tamanio <= (b.inicio - fin):
                            if (peor == None) or (peor < (b.inicio - fin)):
                                peor = (b.inicio - fin)
                                inicio = fin   
                        fin = b.tamanio + b.inicio
                if (self.memoria.longitud - fin) >= dato.tamanio:
                    if peor == None:
                        dato.inicio = fin
                    else:
                        if peor >= (self.memoria.longitud - fin):
                            dato.inicio = inicio #Si encontro un lugar, coloca al bloque
                        else:
                            dato.inicio = fin #Si no encuentra, coloca al bloque en el final
                else:
                    dato.inicio = inicio 


class MemoriaAlumno(Memoria):

    def combinar(self):
        """Combinar bloques adyacentes"""
        raise NotImplementedError

    def compactar(self):
        self.datos.sort(key=lambda x: x.inicio)
        if len(self.datos) != 0:
            fin = 0
            for b in self.datos:
                if b.id_proceso != None:
                    if b.inicio > fin:
                        b.inicio = fin
                        #Liberamos el espacio encontrado
                        self.valores = (
                            self.valores[:b.inicio] +
                            str(b.id_proceso)[0] * b.tamanio +
                            self.valores[b.inicio + b.tamanio:]
                        )
                    fin = b.inicio + b.tamanio
                    bloque = b
            #Borramos el id de los procesos que compactamos
            self.valores = (
                self.valores[:bloque.inicio + bloque.tamanio] + " " * bloque.tamanio +
                self.valores[self.longitud:]
            )
            bloque.id_proceso = None
                


if __name__ == '__main__':

    for algoritmo in [PrimerAjuste(), MejorAjuste(), PeorAjuste()]:
        try:
            print "*" * 80
            print "Ejecutando con: %s" % algoritmo
            print ""

            memoria = MemoriaAlumno(50)
            memoria.usar(algoritmo)

            # Cargar los datos de un archivo
            datos = open('datos.pkl', 'r')
            lista_datos = pickle.load(datos)
            datos.close()

            # Llamar al cargar de la memoria
            print "Cargando los datos generales"
            for dato in lista_datos:
                memoria.colocar(dato)

            # Estado inicial de la memoria
            print "Estado inicial de la memoria"
            print memoria

            # Procesamiento
            if len(memoria.datos) > 0:
                b = memoria.datos[1]
                print "\nLiberar %s" % b
                memoria.liberar(b)
                print memoria
            else:
                print "No hay datos en la memoria para liberar (ERROR)"

            d6 = Bloque(6, 2)
            print "\nColocar %s" % d6
            memoria.colocar(d6)
            print memoria

            print ""
            if len(memoria.datos) > 4:
                for pos in [4, 1, 3]:
                    b = memoria.datos[pos]
                    print "Liberar %s" % b
                    memoria.liberar(b)
                print memoria
            else:
                print "No hay datos suficientes para liberar (ERROR)"

            d7 = Bloque(7, 4)
            print "\nColocar %s" % d7
            memoria.colocar(d7)
            print memoria

            #Probamos cambiar el tamaño de este bloque de 2 a 6
            d8 = Bloque(8, 2)
            print "\nColocar %s" % d8
            memoria.colocar(d8)
            print memoria

            d9 = Bloque(9, 10)
            print "\nColocar %s" % d9
            memoria.colocar(d9)
            print memoria

            if len(memoria.datos) > 2:
                b = memoria.datos[-2]
                print "\nLiberar %s" % b
                memoria.liberar(b)
                print memoria
            else:
                print "No hay datos suficientes para liberar (ERROR)"

            #Liberamos el bloque de id 1
            """if len(memoria.datos) > 0:
                b = memoria.datos[0]
                print "\nLiberar %s" % b
                memoria.liberar(b)
                print memoria
            else:
                print "No hay datos en la memoria para liberar (ERROR)"
                """

            #Agregamos el proceso B de tamaño 1
            """d14 = Bloque("B", 1)
            print "\nColocar %s" % d14
            memoria.colocar(d14)
            print memoria"""
                
            d10 = Bloque(0, 2)
            print "\nColocar %s" % d10
            memoria.colocar(d10)
            print memoria

            d11 = Bloque('A', 2)
            print "\nColocar %s" % d11
            memoria.colocar(d11)
            print memoria

            d12 = Bloque('X', 200)
            print "\nColocar %s" % d12
            memoria.colocar(d12)
            print memoria

            d12 = Bloque('Y', 88)
            print "\nColocar %s" % d12
            memoria.colocar(d12)
            print memoria

            d13 = Bloque('Z', 20)
            print "\nColocar %s" % d13
            memoria.colocar(d13)
            print memoria

            # Descomentar las llamadas a las funciones una vez condificadas
            # Combinar
            # memoria.combinar()
            # Compactar
            memoria.compactar()
            print memoria
            
        except NotImplementedError:
            print "El algoritmo no esta implementado"
