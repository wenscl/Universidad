#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>

// Eventos
#define ArriboAvion				1
#define ArriboAduana			2
#define FinAduana				3
#define FinRevisionEquipaje		4


//Colas y Listas
#define AgenteAduana1			1
#define AgenteAduana2			2
#define	AgenteEquipaje			3
#define ColaAduana				4
#define ColaEquipaje			5

// Sampst
#define DemoraPasajerosAduana	1
#define DemoraPasajerosEquipaje	2

// Posiciones de Transfer
#define _Tiempo					1
#define _TipoEvento				2
#define _Agente					3

// Variables
float interarribo_aduana, servicio_aduana, interarribo_avion, servicio_equipaje_min, servicio_equipaje_max, arribo_pasajeros_min,
	arribo_pasajeros_max;
int fin_simulacion, cantidad_pasajeros, aleatorio_min, aleatorio_max, nro_aleatorio, contador, cant_equipaje, total_pasajeros;

// Rutinas
int main();
void Inicializacion(void);
void RutinaArriboAvion(void);
void RutinaArriboAduana(void);
void RutinaFinAduana(void);
void RutinaFinRevisionEquipaje(void);
void GenerarFinAduana(int agente);
void Reporte(void);

//Funcion Principal
int main()  
{
	// Inicializar SimLib
	init_simlib();

	// Rutina Inicializar
	Inicializacion();

	// Comienzo Simulacion
	while (sim_time <= fin_simulacion || cantidad_pasajeros > 0)
	{
		// Rutina Timing
		timing();

		// Determinar tipo de evento y llamar a su rutina
		switch(next_event_type)
		{
			case ArriboAvion:
				RutinaArriboAvion();
				break;
			case ArriboAduana:
				RutinaArriboAduana();
				break;
			case FinAduana:
				RutinaFinAduana();
				break;
			case FinRevisionEquipaje:
				RutinaFinRevisionEquipaje();
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
	fin_simulacion = 10080;
	interarribo_aduana = 0.2;
	servicio_aduana = 0.55;
	interarribo_avion = 180;
	servicio_equipaje_min = 3;
	servicio_equipaje_max = 6;
	arribo_pasajeros_min = 240;
	arribo_pasajeros_max = 350;
	cantidad_pasajeros = 0;
	aleatorio_min = 1;
	aleatorio_max = 10;
	nro_aleatorio = uniform(aleatorio_min, aleatorio_max, ArriboAduana);
	contador = 0;
	cant_equipaje = 0;
	total_pasajeros = 0;

	// Generar eventos iniciales
	// Arribo avion
	transfer[_Tiempo] = sim_time + expon(interarribo_avion, ArriboAvion);
	transfer[_TipoEvento] = ArriboAvion;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaArriboAvion(void)
{
	// Arribo pasajero aduana
	if (cantidad_pasajeros == 0)
	{
		transfer[_Tiempo] = sim_time + expon(interarribo_aduana, ArriboAduana);
		transfer[_TipoEvento] = ArriboAduana;
		list_file(INCREASING, LIST_EVENT);
	}

	// Cantidad de pasajeros que llegaron
	cantidad_pasajeros += uniform(arribo_pasajeros_min, arribo_pasajeros_max, ArriboAvion);
	total_pasajeros += cantidad_pasajeros;
	cantidad_pasajeros--;

	// Generar siguiente arribo avion
	float sig_arribo_avion = sim_time + expon(interarribo_avion, ArriboAvion);
	if (sig_arribo_avion < fin_simulacion)
	{
		transfer[_Tiempo] = sig_arribo_avion;
		transfer[_TipoEvento] = ArriboAvion;
		list_file(INCREASING, LIST_EVENT);
	}
}

void RutinaArriboAduana()
{
	contador++;
	if (contador == nro_aleatorio)
	{
		nro_aleatorio = uniform(aleatorio_min, aleatorio_max, ArriboAduana);
		contador = 0;
		transfer[_Tiempo] = sim_time;
		if (list_size[AgenteEquipaje] > 0)
		{
			list_file(LAST, ColaEquipaje);
		}
		else
		{
			list_file(FIRST, AgenteEquipaje);
			sampst(0, DemoraPasajerosEquipaje);

			// Determinar fin revision equipaje
			transfer[_Tiempo] = sim_time + uniform(servicio_equipaje_min, servicio_equipaje_max, FinRevisionEquipaje);
			transfer[_TipoEvento] = FinRevisionEquipaje;
			list_file(INCREASING, LIST_EVENT);
		}
		cant_equipaje++;
	}
	else
	{
		transfer[_Tiempo] = sim_time;
		if (list_size[AgenteAduana1] == 0)
		{
			transfer[_Agente] = AgenteAduana1;
			sampst(0, DemoraPasajerosAduana);
			list_file(FIRST, AgenteAduana1);

			// Determinar fin servicio aduana
			GenerarFinAduana(AgenteAduana1);
		}
		else if (list_size[AgenteAduana2] == 0)
		{
			transfer[_Agente] = AgenteAduana2;
			sampst(0, DemoraPasajerosAduana);
			list_file(FIRST, AgenteAduana2);

			// Determinar fin servicio aduana
			GenerarFinAduana(AgenteAduana2);
		}
		else
		{
			list_file(LAST, ColaAduana);
		}
	}

	// Generar siguiente arribo pasajero aduana
	if (cantidad_pasajeros > 0)
	{
		transfer[_Tiempo] = sim_time + expon(interarribo_aduana, ArriboAduana);
		transfer[_TipoEvento] = ArriboAduana;
		list_file(INCREASING, LIST_EVENT);
		cantidad_pasajeros--;
	}
}

void RutinaFinAduana(void)
{
	int agente = transfer[_Agente];
	list_remove(FIRST, agente);

	// Atender a otra persona
	if (list_size[ColaAduana] > 0)
	{
		list_remove(FIRST, ColaAduana);
		sampst(sim_time - transfer[_Tiempo], DemoraPasajerosAduana);
		transfer[_Tiempo] = sim_time;
		list_file(FIRST, agente);

		// Determinar fin servicio aduana
		GenerarFinAduana(agente);
	}
}

void RutinaFinRevisionEquipaje(void)
{
	list_remove(FIRST, AgenteEquipaje);
	if (list_size[ColaEquipaje] > 0)
	{
		list_remove(FIRST, ColaEquipaje);
		sampst(sim_time - transfer[_Tiempo], DemoraPasajerosEquipaje);
		transfer[_Tiempo] = sim_time;
		list_file(FIRST, AgenteEquipaje);

		// Determinar fin revision equipaje
		transfer[_Tiempo] = sim_time + uniform(servicio_equipaje_min, servicio_equipaje_max, FinRevisionEquipaje);
		transfer[_TipoEvento] = FinRevisionEquipaje;
		list_file(INCREASING, LIST_EVENT);
	}
}

void GenerarFinAduana(int agente)
{
	transfer[_Tiempo] = sim_time + expon(servicio_aduana, FinAduana);
	transfer[_TipoEvento] = FinAduana;
	transfer[_Agente] = agente;
	list_file(INCREASING, LIST_EVENT);
}

// Generar Reporte de Simulación
void Reporte(void)
{
	printf("ESTADISTICOS:\n\n");
	
	// Cantidad de pasajeros
	printf("Cantidad total de pasajeros: %.i\n\n", total_pasajeros);

	// - Utilización de cada uno de los agentes.
	filest(AgenteAduana1);
	printf("Utilizacion del agente de aduana 1: %.2f%%\n\n", transfer[1] * 100);
	filest(AgenteAduana2);
	printf("Utilizacion del agente de aduana 2: %.2f%%\n\n", transfer[1] * 100);
	filest(AgenteEquipaje);
	printf("Utilizacion del agente de revision de equipaje: %.2f%%\n\n", transfer[1] * 100);

	// - Demora media de los pasajeros en cada una de las colas.
	sampst(0, -DemoraPasajerosAduana);
	printf("Demora de los pasajeros en la cola de aduana: %.2f minutos\n\n", transfer[1]);
	sampst(0, -DemoraPasajerosEquipaje);
	printf("Demora de los pasajeros en la cola de revision de equipaje: %.2f minutos\n\n", transfer[1]);

	// - Número medio en cola de pasajeros en las dos colas.
	printf("Numero medio de pasajeros en ambas colas: %.2f\n\n", filest(ColaAduana) + filest(ColaEquipaje));

	// - Porcentaje de pasajeros a los que se les revisa el equipaje.
	printf("Porcentaje de pasajeros a los que se les revisa el equipaje: %.2f%%\n\n", (float)cant_equipaje / total_pasajeros * 100);
}