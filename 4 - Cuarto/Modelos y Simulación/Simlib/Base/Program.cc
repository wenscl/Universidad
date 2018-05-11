#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>

// Eventos
#define EjemploEvento				1	// Descripcion.

//Colas y Listas
#define EjemploServidor				1	// Descripcion.
#define EjemploCola					2	// Descripcion.

// Sampst
#define EjemploDemora				1	// Descripcion.

// Posiciones de Transfer
#define EjemploT1Tiempo				1

// Variables
int ejemplo;

// Rutinas
int main();
void Inicializacion(void);
void EjemploRutina(void);
void EjemploNuevoEvento(int algo);
void Reporte(void);

//Funcion Principal
int main()  
{
	// Inicializar SimLib
	init_simlib();

	// Rutina Inicializar
	Inicializacion();

	// Comienzo Simulacion
	while (sim_time <= 1000000)  // TODO: Setear fin de simulacion
	{
		// Rutina Timing
		timing();

		// Determinar tipo de evento y llamar a su rutina
		switch(next_event_type)
		{
			case EjemploEvento:
				EjemploRutina();
				break;
        }
	}

	// Fin de Simulación - Generar Reporte
	Reporte();

	// Finalizar Simulación
	system("pause");
}

// Inicializar Sistema
void Inicializacion(void)
{
	// Inicializar variables del sistema
	
	// Generar eventos iniciales
}

void EjemploRutina(void)
{
}

void EjemploNuevoEvento(int algo)
{
}

// Generar Reporte de Simulación
void Reporte(void)
{
	// Impresión en Pantalla
	printf("Titulo \n\n");
	printf("Estadisticos:\n\n");


	// Utilizacion 
	filest(EjemploServidor);
	printf("Utilizacion del Servidor: %.2f %%\n\n", transfer[1] * 100);

	// Tiempo de espera 
	sampst(0, -EjemploDemora);
	printf("Tiempo medio de espera: %.2f segundos\n", transfer[1]);

	// Cantidad media en cola de espera
	filest(EjemploCola);
	printf("\nCantidad media de pedidos en Cola de espera: %.2f\n", transfer[1]);
}