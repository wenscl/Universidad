/* Modelo MM1 - Un Servidor, Una Cola  */


#include "simlib.c"
#include <stdio.h>
#include <stdlib.h> 

//Eventos
#define ArriboPiezas			1
#define LlegadaMontacarga		2
#define ArriboAlmacen			3

//Colas
#define Montacargas				1
#define Estacion1				2
#define Estacion2				3
#define Estacion3				4
#define Estacion4				5

//Demoras
#define Demora_Estacion1		6
#define Demora_Estacion2		7
#define Demora_Estacion3		8
#define Demora_Estacion4		9

// Declaracion de variables
int interarribo_estaciones, interarribo_almacen, estacion1y2, estacion3y4, carga_actual, tiempo_fin, capacidad, vueltas, bandera;

// Declaracion de Funciones
void Inicializar(void);
void Rutina_ArriboPiezas(void);
void Rutina_LlegadaMontacarga(void);
void Rutina_ArriboAlmacen(void);
void Reporte(void);

int main()
{
	// Inicializar Simlib
	init_simlib();

	// Establecer maximo numero de atributos utilizados en el transfer
	maxatr = 4;

	// Inicializar el Sistema
	Inicializar();

	while (sim_time < tiempo_fin)
	{
		// Determinar proximo Evento
		timing();
		switch (next_event_type)
		{
		case ArriboPiezas:
			Rutina_ArriboPiezas();
			break;
		case LlegadaMontacarga:
			Rutina_LlegadaMontacarga();
			break;
		case ArriboAlmacen:
			Rutina_ArriboAlmacen();
			break;
		}
	}
	// Generar reporte
	Reporte();
	system("pause");
}

void Inicializar(void)  // Inicializar el Sistema
{
	//Definicion de variables
	tiempo_fin = 432000;
	interarribo_estaciones = 30;
	interarribo_almacen = 300;
	estacion1y2 = 300;
	estacion3y4 = 180;
	capacidad = 6;
	carga_actual = 0;
	bandera = 0;
	vueltas = 0;

	// Cargar la lista de eventos con los eventos que inicializan la simulacion
	for (int i = 0; i < 2; i++)
	{
		transfer[1] = sim_time + expon(estacion1y2, ArriboPiezas);
		transfer[2] = ArriboPiezas;
		transfer[3] = i + 1;
		list_file(INCREASING, LIST_EVENT);
	}
	for (int i = 1; i < 3; i++)
	{
		transfer[1] = sim_time + expon(estacion3y4, ArriboPiezas);
		transfer[2] = ArriboPiezas;
		transfer[3] = i + 2;
		list_file(INCREASING, LIST_EVENT);
	}

	transfer[1] = sim_time + interarribo_estaciones;
	transfer[2] = LlegadaMontacarga;
	transfer[3] = 1;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_ArriboPiezas(void)
{
	int estacion = transfer[3];
	transfer[1] = sim_time;
	int funcion = 0;

	switch (estacion)
	{
	case 1:
		list_file(LAST, Estacion1);
		funcion = estacion1y2;
		break;
	case 2: 
		list_file(LAST, Estacion2);
		funcion = estacion1y2;
		break;
	case 3:
		list_file(LAST, Estacion3);
		funcion = estacion3y4;
		break;
	case 4:
		list_file(LAST, Estacion4);
		funcion = estacion3y4;
		break;
	}
	
	// Determinar próximo arribo pieza
	transfer[1] = sim_time + expon(funcion, ArriboPiezas);
	transfer[2] = ArriboPiezas;
	transfer[3] = estacion;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_LlegadaMontacarga(void)
{
	int estacion = transfer[3];
	int cola = 0;
	int tamanio = 0;
	int demora = 0;
	switch (estacion)
	{
	case 1:
		cola = Estacion1;
		tamanio = 1;
		demora = Demora_Estacion1;
		break;
	case 2:
		cola = Estacion2;
		tamanio = 2;
		demora = Demora_Estacion2;
		break;
	case 3:
		cola = Estacion3;
		tamanio = 3;
		demora = Demora_Estacion3;
		break;
	case 4:
		cola = Estacion4;
		tamanio = 3;
		demora = Demora_Estacion4;
		break;
	}

	while (list_size[cola] > 0 && carga_actual + tamanio <= capacidad)
	{
		list_remove(FIRST, cola);
		sampst(sim_time - transfer[1], demora);
		list_file(LAST, Montacargas);
		carga_actual += tamanio;
	}

	// Proxima llegada montacargas
	if (estacion == 4)
	{
		// Menos del 50%
		if (carga_actual < capacidad / 2)
		{
			transfer[1] = sim_time;
			transfer[2] = LlegadaMontacarga;
			transfer[3] = 1;
			bandera = 1;
		}
		else
		{
			transfer[1] = sim_time + interarribo_almacen;
			transfer[2] = ArriboAlmacen;
		}
	}
	else
	{
		transfer[1] = sim_time + interarribo_estaciones;
		transfer[2] = LlegadaMontacarga;
		transfer[3] = estacion + 1;
	}
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_ArriboAlmacen(void)
{
	if (bandera = 1)
	{
		vueltas++;
		bandera = 0;
	}

	while (list_size[Montacargas] > 0)
	{
		list_remove(FIRST, Montacargas);
	}
	carga_actual = 0;

	transfer[1] = sim_time + interarribo_almacen;
	transfer[2] = LlegadaMontacarga;
	transfer[3] = 1;
	list_file(INCREASING, LIST_EVENT);
}

void Reporte(void)
{
	printf("ESTADISTICAS\n");

	// Demora Media y Maxima en cada estacion
	sampst(0, -Demora_Estacion1);
	printf("\nDemora Media de espera en la Estacion 1: %.3f \n ", transfer[1]);
	printf("\nDemora Maxima de espera en la Estacion 1: %.3f \n ", transfer[3]);
	sampst(0, -Demora_Estacion2);
	printf("\nDemora Media de espera en la Estacion 2: %.3f \n ", transfer[1]);
	printf("\nDemora Maxima de espera en la Estacion 2: %.3f \n ", transfer[3]);
	sampst(0, -Demora_Estacion3);
	printf("\nDemora Media de espera en la Estacion 3: %.3f \n ", transfer[1]);
	printf("\nDemora Maxima de espera en la Estacion 3: %.3f \n ", transfer[3]);
	sampst(0, -Demora_Estacion4);
	printf("\nDemora Media de espera en la Estacion 4: %.3f \n ", transfer[1]);
	printf("\nDemora Maxima de espera en la Estacion 4: %.3f \n ", transfer[3]);

	// Numerio Medio en cada cola
	filest(Estacion1);
	printf("\nNumero Medio de espera en la Estacion 1: %.3f \n ", transfer[1]);
	filest(Estacion2);
	printf("\nNumero Medio de espera en la Estacion 2: %.3f \n ", transfer[1]);
	filest(Estacion3);
	printf("\nNumero Medio de espera en la Estacion 3: %.3f \n ", transfer[1]);
	filest(Estacion4);
	printf("\nNumero Medio de espera en la Estacion 4: %.3f \n ", transfer[1]);

	// Cantidad Promedio de piezas transportadas por el Montacargas
	filest(Montacargas);
	printf("\nCantidad Promedio de piezas transportadas por el Montacargas: %.3f \n ", transfer[1]);

	// Procentaje de ocasiones en las que el montacargas realiza el circuito mas de una vez
	printf("\nProcentaje de ocasiones en las que el montacargas realiza el circuito mas de una vez: %3.f \n ", vueltas);
}