#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>

// Eventos
#define ArriboProceso			1
#define FinProceso				2
#define Desbloquear				3

//Colas y Listas
#define Procesador				1
#define ColaListos				2
#define ColaBloqueados			3
#define AuxEvento				4	// Para cancelar eventos
#define ColaListosNormales		5	// Para sacar el numero medio en la cola listos

// Sampst
#define DemoraListos			1

// Posiciones de Transfer
#define _Tiempo					1
#define _Evento					2
#define _Prioridad				3
#define	_FinProcesamiento		4
#define _TiempoProcesamiento	5
#define _Bloqueado				6

// Variables
int tiempo_simulacion, prioridad, cantidad_procesos, cantidad_procesos_normales, cantidad_desplazados;
float interarribo_proceso, servicio_proceso, servicio_bloqueado_min, servicio_bloqueado_max;

// Rutinas
int main();
void Inicializacion(void);
void RutinaArriboProceso(void);
void RutinaFinProceso(void);
void RutinaDesbloquear(void);
void Reporte(void);

//Funcion Principal
int main()  
{
	// Inicializar SimLib
	init_simlib();

	// Rutina Inicializar
	Inicializacion();

	// Comienzo Simulacion
	while (sim_time <= tiempo_simulacion)
	{
		// Rutina Timing
		timing();

		// Determinar tipo de evento y llamar a su rutina
		switch(next_event_type)
		{
			case ArriboProceso:
				cantidad_procesos++;
				RutinaArriboProceso();
				break;
			case FinProceso:
				RutinaFinProceso();
				break;
			case Desbloquear:
				RutinaDesbloquear();
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
	tiempo_simulacion = 28800;
	interarribo_proceso = 2.3;
	servicio_proceso = 3.8;
	servicio_bloqueado_min = 0.9;
	servicio_bloqueado_max = 1.4;
	prioridad = 0;
	cantidad_procesos, cantidad_procesos_normales, cantidad_desplazados = 0;

	// Generar eventos iniciales
	// Arribo proceso
	transfer[_Tiempo] = sim_time + expon(interarribo_proceso, ArriboProceso);
	transfer[_Evento] = ArriboProceso;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaArriboProceso(void)
{
	// Asignar prioridad
	// Prioridad alta = 1, prioridad baja = 0
	float probabilidad = lcgrand(ArriboProceso);
	if (probabilidad <= 0.2)
	{
		transfer[_Prioridad] = 1;
		prioridad = 1;
	}
	else
	{
		transfer[_Prioridad] = 0;
		prioridad = 0;
		cantidad_procesos_normales++;
	}

	if (list_size[Procesador] == 0)
	{
		sampst(0, DemoraListos);
		float tiempo_servicio = expon(servicio_proceso, FinProceso);
		transfer[_TiempoProcesamiento] = 0;
		transfer[_FinProcesamiento] = tiempo_servicio;
		// ver si se va a bloquear
		float probabilidad = lcgrand(14);
		if (probabilidad <= 0.26)
		{
			transfer[_Bloqueado] = true;
		}
		else
		{
			transfer[_Bloqueado] = false;
		}
		list_file(FIRST, Procesador);

		// Generar fin del procesamiento
		if (probabilidad <= 0.26)
		{
			transfer[_Tiempo] = sim_time + tiempo_servicio / 2;
			transfer[_Bloqueado] = true;
		}
		else
		{
			transfer[_Tiempo] = sim_time + tiempo_servicio;
			transfer[_Bloqueado] = false;
		}
		transfer[_Evento] = FinProceso;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		if (prioridad == 0)
		{
			float tiempo_servicio = expon(servicio_proceso, FinProceso);
			transfer[_TiempoProcesamiento] = 0;
			transfer[_FinProcesamiento] = tiempo_servicio;
			// ver si se va a bloquear
			float probabilidad = lcgrand(14);
			if (probabilidad <= 0.26)
			{
				transfer[_Bloqueado] = true;
			}
			else
			{
				transfer[_Bloqueado] = false;
			}
			list_file(LAST, ColaListos);

			transfer[_Tiempo] = sim_time;
			list_file(FIRST, ColaListosNormales);
		}
		else
		{
			list_remove(FIRST, Procesador);
			float tiempo_inicial = transfer[_Tiempo];
			if (transfer[_Prioridad] == 0)
			{
				// Sacar y pasar a la cola
				transfer[_TiempoProcesamiento] = sim_time - transfer[_Tiempo] + transfer[_TiempoProcesamiento];
				list_file(FIRST, ColaListos);
				cantidad_desplazados++;
				transfer[_Tiempo] = sim_time;
				list_file(FIRST, ColaListosNormales);

				// Eliminar fin proceso
				event_cancel(FinProceso);
				while (transfer[_Tiempo] != tiempo_inicial)
				{
					list_file(FIRST, AuxEvento);
					event_cancel(FinProceso);
				}
				while (list_size[AuxEvento] > 0)
				{
					list_remove(FIRST, AuxEvento);
					list_file(INCREASING, LIST_EVENT);
				}

				// Ocupar procesador
				sampst(0, DemoraListos);
				float tiempo_servicio = expon(servicio_proceso, FinProceso);
				transfer[_Tiempo] = sim_time;
				transfer[_Prioridad] = 1;
				transfer[_TiempoProcesamiento] = 0;
				transfer[_FinProcesamiento] = tiempo_servicio;

				// Ver si se va a bloquear
				float probabilidad = lcgrand(14);
				if (probabilidad <= 0.26)
				{
					transfer[_Bloqueado] = true;
				}
				else
				{
					transfer[_Bloqueado] = false;
				}
				list_file(FIRST, Procesador);

				// Generar el fin
				if (probabilidad <= 0.26)
				{
					transfer[_Tiempo] = sim_time + tiempo_servicio / 2;
					transfer[_Bloqueado] = true;
				}
				else
				{
					transfer[_Tiempo] = sim_time + tiempo_servicio;
					transfer[_Bloqueado] = false;
				}
				transfer[_Evento] = FinProceso;
				list_file(INCREASING, LIST_EVENT);
			}
			else
			{
				list_file(FIRST, Procesador);

				float tiempo_servicio = expon(servicio_proceso, FinProceso);
				transfer[_Tiempo] = sim_time;
				transfer[_Prioridad] = 1;
				transfer[_TiempoProcesamiento] = 0;
				transfer[_FinProcesamiento] = tiempo_servicio;
				// ver si se va a bloquear
				float probabilidad = lcgrand(14);
				if (probabilidad <= 0.26)
				{
					transfer[_Bloqueado] = true;
				}
				else
				{
					transfer[_Bloqueado] = false;
				}
				list_file(LAST, ColaListos);
			}
		}
	}

	// Siguiente arribo proceso
	transfer[_Tiempo] = sim_time + expon(interarribo_proceso, ArriboProceso);
	transfer[_Evento] = ArriboProceso;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaFinProceso(void)
{
	list_remove(FIRST, Procesador);
	float fin_procesamiento = transfer[_FinProcesamiento];
	float tiempo_procesamiento = sim_time - transfer[_Tiempo] + transfer[_TiempoProcesamiento];
	if (transfer[_Bloqueado])
	{
		transfer[_TiempoProcesamiento] = tiempo_procesamiento;
		list_file(LAST, ColaBloqueados);
		// Generar fin bloqueo
		transfer[_Tiempo] = sim_time + uniform(servicio_bloqueado_min, servicio_bloqueado_max, Desbloquear);
		transfer[_Evento] = Desbloquear;
		transfer[_FinProcesamiento] = fin_procesamiento;
		list_file(INCREASING, LIST_EVENT);
	}
	
	if (list_size[ColaListos] > 0)
	{
		list_remove(FIRST, ColaListos);
		sampst(sim_time - transfer[_Tiempo] - transfer[_TiempoProcesamiento], DemoraListos);
		float fin_procesamiento = transfer[_FinProcesamiento];
		float tiempo_procesamiento = transfer[_TiempoProcesamiento];
		bool bloqueado = transfer[_Bloqueado];
		int prioridad = transfer[_Prioridad];
		list_file(FIRST, Procesador);

		if (prioridad == 0)
		{
			list_remove(FIRST, ColaListosNormales);
		}

		if (bloqueado)
		{
			// Generar fin de procesamiento
			transfer[_Tiempo] = sim_time + fin_procesamiento / 2 - tiempo_procesamiento;
			transfer[_Evento] = FinProceso;
			transfer[_Bloqueado] = true;
			list_file(INCREASING, LIST_EVENT);
		}
		else
		{
			// Generar fin de procesamiento
			transfer[_Tiempo] = sim_time + fin_procesamiento - tiempo_procesamiento;
			transfer[_Evento] = FinProceso;
			transfer[_Bloqueado] = false;
			list_file(INCREASING, LIST_EVENT);
		}
	}
}

void RutinaDesbloquear(void)
{
	list_remove(FIRST, ColaBloqueados);
	float tiempo_inicial = transfer[_Tiempo];
	int prioridad = transfer[_Prioridad];
	float fin_procesamiento = transfer[_FinProcesamiento];
	float tiempo_procesamiento = transfer[_TiempoProcesamiento];
	if (list_size[Procesador] == 0)
	{
		list_file(FIRST, Procesador);

		// Generar fin del procesamiento
		transfer[_Tiempo] = fin_procesamiento;
		transfer[_Bloqueado] = true;
		transfer[_Evento] = FinProceso;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		if (prioridad == 0)
		{
			list_file(LAST, ColaListos);
		}
		else
		{
			list_remove(FIRST, Procesador);
			if (transfer[_Prioridad] == 0)
			{
				// Pasar a la cola
				transfer[_TiempoProcesamiento] = sim_time - transfer[_Tiempo] + transfer[_TiempoProcesamiento];
				float inicial = transfer[_Tiempo];
				list_file(FIRST, ColaListos);

				// Eliminar fin proceso
				event_cancel(FinProceso);
				while (transfer[_Tiempo] != inicial)
				{
					list_file(FIRST, AuxEvento);
					event_cancel(FinProceso);
				}
				while (list_size[AuxEvento] > 0)
				{
					list_remove(FIRST, AuxEvento);
					list_file(INCREASING, LIST_EVENT);
				}

				// Ocupar procesador
				transfer[_Tiempo] = tiempo_inicial;
				transfer[_Prioridad] = 1;
				transfer[_TiempoProcesamiento] = tiempo_procesamiento;
				transfer[_FinProcesamiento] = fin_procesamiento;
				transfer[_Bloqueado] = false;
				list_file(FIRST, Procesador);

				// Generar el fin
				transfer[_Tiempo] = fin_procesamiento;
				transfer[_Bloqueado] = false;
				transfer[_Evento] = FinProceso;
				list_file(INCREASING, LIST_EVENT);
			}
			else
			{
				list_file(FIRST, Procesador);

				float tiempo_servicio = expon(servicio_proceso, FinProceso);
				transfer[_Tiempo] = sim_time;
				transfer[_Prioridad] = 1;
				transfer[_TiempoProcesamiento] = 0;
				transfer[_FinProcesamiento] = tiempo_servicio;
				transfer[_Bloqueado] = false;
				list_file(LAST, ColaListos);
			}
		}
	}
}

// Generar Reporte de Simulación
void Reporte(void)
{
	// Impresión en Pantalla
	printf("Estadisticos:\n\n");

	printf("Cantidad de procesos: %.2f segundos\n", cantidad_procesos);

	sampst(0, -DemoraListos);
	printf("\nDemora media de los procesos en cola de listos: %.2f segundos\n", transfer[1]);

	filest(ColaListosNormales);
	printf("\nNumero medio de procesos normales en la cola de listos: %.2f\n", transfer[1]);

	filest(ColaBloqueados);
	printf("\nNumero medio de procesos en la cola de bloqueados: %.2f\n", transfer[1]);

	printf("\nPorcentaje de procesos normales que deben dejar el procesador: %.2f %%\n", float(cantidad_desplazados) / cantidad_procesos_normales);

	filest(Procesador);
	printf("\nPorcentaje de utilizacion del procesador: %.2f %%\n", transfer[1]);
}
