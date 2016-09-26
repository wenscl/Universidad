/* Modelo MM1 - Un Servidor, Una Cola  */


#include "simlib.c"
#include <stdio.h>
#include <stdlib.h> 

//Eventos
#define ArriboPersonaA    1 // Arribo Personas Aeropuerto  
#define ArriboPersonaR    2 // Arribo Personas Remiseria 
#define LlegadaColeA      3 // Llegada Colectivo Aeropuerto
#define LlegadaColeR      4 // Llegada Colectivo Remiseria
#define MantenimientoCole 5 // Manteminiento del Colectivo

//Colas
#define Colectivo         1 // "Servidor"
#define ColaR             2 // Cola Remis
#define ColaA			  3 // Cola Aeropuerto

#define Demora_colaR      1 // Sampst 1: Demora en Cola Remis
#define Demora_colaA      2 // Sampst 2: Demora en Cola Aeropuerto

// Declaracion de variables
float media_interarribos_remises, media_servicio_min, media_servicio_max, media_interarribos_aeropuerto;
int tiempo_fin, i;
bool mantenimiento;

// Declaracion de Funciones
void Inicializar(void);
void Rutina_arribosPersonaA(void);
void Rutina_arribosPersonaR(void);
void Rutina_llegadaColeA(void);
void Rutina_llegadaColeR(void);
void Rutina_mantenimientoCole(void);
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
		switch( next_event_type )
		{
			case ArriboPersonaA:
				Rutina_arribosPersonaA();
				break;
			case ArriboPersonaR:
				Rutina_arribosPersonaR();
				break; 
			case LlegadaColeR:
				Rutina_llegadaColeR();
				break;
			case LlegadaColeA:
				Rutina_llegadaColeA();
				break;
			case MantenimientoCole:
				Rutina_mantenimientoCole();
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
	tiempo_fin = 10080;
	media_interarribos_aeropuerto = 12.8;
	media_interarribos_remises = 7.9;
	media_servicio_min = 10;
	media_servicio_max = 15;
	mantenimiento = false;
	// Probabilidades de que lleguen 1, 2, 3 o 4 personas
	prob_distrib[1] = 0.3;
	prob_distrib[2] = 0.75;
	prob_distrib[3] = 0.9;
	prob_distrib[4] = 1;

	// Cargar la lista de eventos con los eventos que inicializan la simulacion
	transfer[1] = sim_time + 30;
	transfer[2] = LlegadaColeR;
	list_file(INCREASING,LIST_EVENT);

	transfer[1] = sim_time + expon(media_interarribos_aeropuerto, ArriboPersonaA);
	transfer[2] = ArriboPersonaA;
	list_file(INCREASING, LIST_EVENT);
	
	transfer[1] = sim_time + expon(media_interarribos_remises, ArriboPersonaR);
	transfer[2] = ArriboPersonaR;
	list_file(INCREASING, LIST_EVENT);

	transfer[1] = sim_time + 240;
	transfer[2] = MantenimientoCole;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_arribosPersonaA(void) 
{
	// Determinar cuantos pasajeros llegan (1,2,3, o 4)
	int cantPasajeros = random_integer(prob_distrib, ArriboPersonaA);

	// Determinar proximo Arribo Aeropuerto
	transfer[1] = sim_time + expon(media_interarribos_aeropuerto, ArriboPersonaA);
	transfer[2] = ArriboPersonaA;
	list_file(INCREASING, LIST_EVENT);
	
	// Cargar pasajeros en cola
	for (int i = 0; i < cantPasajeros; i++)
	{
		transfer[1] = sim_time;
		list_file(LAST, ColaA);
	}
}

void Rutina_arribosPersonaR(void)
{
	// Determinar cuantos pasajeros llegan
	int cantPasajeros = random_integer(prob_distrib, ArriboPersonaR);

	// Determinar proximo Arribo Remiseria
	transfer[1] = sim_time + expon(media_interarribos_remises, ArriboPersonaR);
	transfer[2] = ArriboPersonaR;
	list_file(INCREASING, LIST_EVENT);

	// Cargar pasajeros en cola
	for (int i = 0; i < cantPasajeros; i++)
	{
		transfer[1] = sim_time;
		list_file(LAST, ColaR);
	}
}

void Rutina_mantenimientoCole(void)
{
	mantenimiento = true;
	// Determinar proximo evento Mantenimiento
	transfer[1] = sim_time + 240;
	transfer[2] = MantenimientoCole;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_llegadaColeR(void) 
{
	if (mantenimiento)
	{
		// Generar proximo Arribo Remiseria en 15 minutos
		transfer[1] = sim_time + 15;
		transfer[2] = LlegadaColeR;
		list_file(INCREASING, LIST_EVENT);
		mantenimiento = false;
	}
	else
	{
		// Bajar pasajeros del Colectivo
		while (list_size[Colectivo] > 0)
			list_remove(FIRST, Colectivo);

		// Cargar el Colectivo hasta 25 personas
		while ((list_size[ColaR] > 0) && (list_size[Colectivo] <= 25))
		{
			// Eliminar pasajero de la cola y cargar en Colectivo
			list_remove(FIRST, ColaR);
			sampst(sim_time - transfer[1], Demora_colaR);
			list_file(FIRST, Colectivo);
		}

		// Generar proxima Llegada a Aeropuerto
		transfer[1] = sim_time + uniform(media_servicio_min, media_servicio_max, LlegadaColeA);
		transfer[2] = LlegadaColeA;
		list_file(INCREASING, LIST_EVENT);
	}	
}

void Rutina_llegadaColeA(void) 
{
	// Bajar pasajeros del Colectivo
	while (list_size[Colectivo] > 0)
		list_remove(FIRST, Colectivo);
	
	// Cargar el Colectivo hasta 25 personas
	while ((list_size[ColaA] > 0) && (list_size[Colectivo] <= 25))
	{
		// Eliminar pasajero de la cola y cargar en Colectivo
		list_remove(FIRST, ColaA);
		sampst(sim_time - transfer[1], Demora_colaA);
		list_file(FIRST, Colectivo);
	}
	
	// Generar proxima Llegada a Remiseria
	transfer[1] = sim_time + uniform(media_servicio_min, media_servicio_max, LlegadaColeR);
	transfer[2] = LlegadaColeR;
	list_file(INCREASING, LIST_EVENT);
}

void Reporte(void)
{
	printf("ESTADISTICAS\n");
	sampst(0, -Demora_colaR);
	printf("\nDemora Media en Cola Remiseria: %.3f \n ", transfer[1]);
	printf("\nDemora Maxima en Cola Remiseria: %.3f \n ", transfer[3]);
	sampst(0, -Demora_colaA);
	printf("\nDemora Media en Cola Aeropuerto: %.3f \n ", transfer[1]);
	printf("\nDemora Maxima en Cola Aeropuerto: %.3f \n ", transfer[3]);
	filest(ColaR);
	printf("\nNumero Promedio en Cola Remiseria: %.3f \n ", transfer[1]);
	float promedio_colas = transfer[1];
	filest(ColaA);
	printf("\nNumero Promedio en Cola Aeropuerto: %.3f \n ", transfer[1]);
	promedio_colas += transfer[1];
	printf("\nNumero Promedio en ambas colas: %.3f \n ", promedio_colas);
	filest(Colectivo);
	printf("\nCantidad Promedio de pasajeros transportados: %.3f \n", transfer[1]);
}