#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>

// Eventos
#define InicioJornada	1
#define FinJornada		2
#define ArriboLlamado	3
#define FinLlamado		4
#define Descanso		5
#define FinDescanso		6
#define Falla			7
#define FinEspera		8

//Colas y Listas
#define Operador1		1
#define Operador2		2
#define Operador3		3
#define	Operador4		4
#define Espera			5
#define AuxEspera		6
#define AuxEventos		7

// Sampst
#define DemoraEspera	1
#define TiempoAtencion	2

// Posiciones de Transfer
#define _Tiempo			1
#define _Evento			2
#define _Operador		3
#define _PocaEspera		4

// Variables
float interarribo_llamado;
int llamado_corto_min, llamado_corto_max, llamado_largo, tiempo_descanso, interarribo_descanso, 
	interarribo_falla_min, interarribo_falla_max, falla, tiempo_simulacion, inicio_jornada, fin_jornada,
	cantidad_llamados;
bool recibir_llamado, descanso_operador1, descanso_operador2, descanso_operador3, descanso_operador4;

// Rutinas
int main();
void Inicializacion(void);
void RutinaInicioJornada(void);
void RutinaFinJornada(void);
void RutinaArriboLlamado(void);
void RutinaFinLlamado(void);
void RutinaDescanso(void);
void RutinaFinDescanso(void);
void RutinaFalla(void);
void RutinaFinEspera(void);
void Reporte(void);
void OcuparOperador(int operador);
void GenerarFinLlamado(int operador);
bool DescansoOperador(int operador);
void ActualizarDescanso(int operador, bool valor);

//Funcion Principal
int main()  
{
	// Inicializar SimLib
	init_simlib();

	// Rutina Inicializar
	Inicializacion();

	// Comienzo Simulacion
	while (sim_time <= tiempo_simulacion)  // TODO: Setear fin de simulacion
	{
		// Rutina Timing
		timing();

		// Determinar tipo de evento y llamar a su rutina
		switch(next_event_type)
		{
			case InicioJornada:
				RutinaInicioJornada();
				break;
			case FinJornada:
				RutinaFinJornada();
				break;
			case ArriboLlamado:
				RutinaArriboLlamado();
				cantidad_llamados++;
				break;
			case FinLlamado:
				RutinaFinLlamado();
				break;
			case Descanso:
				RutinaDescanso();
				break;
			case FinDescanso:
				RutinaFinDescanso();
				break;
			case Falla:
				RutinaFalla();
				break;
			case FinEspera:
				RutinaFinEspera();
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
	interarribo_llamado = 3.7;
	llamado_corto_min = 2;
	llamado_corto_max = 5;
	llamado_largo = 15;
	tiempo_descanso = 15;
	interarribo_descanso = 120;
	interarribo_falla_min = 360;
	interarribo_falla_max = 420;
	falla = 0;
	tiempo_simulacion = 7200;
	inicio_jornada = 720;
	fin_jornada = 720;
	recibir_llamado = true;
	descanso_operador1 = false;
	descanso_operador2 = false;
	descanso_operador3 = false;
	descanso_operador4 = false;
	cantidad_llamados = 0;

	// Generar eventos iniciales
	// Arribo llamado
	transfer[_Tiempo] = sim_time + expon(interarribo_llamado, ArriboLlamado);
	transfer[_Evento] = ArriboLlamado;

	list_file(INCREASING, LIST_EVENT);

	// Fin jornada
	transfer[_Tiempo] = sim_time + fin_jornada;
	transfer[_Evento] = FinJornada;

	list_file(INCREASING, LIST_EVENT);

	// Inicio descanso
	transfer[_Tiempo] = sim_time + interarribo_descanso;
	transfer[_Evento] = Descanso;
	transfer[_Operador] = 1;

	list_file(INCREASING, LIST_EVENT);

	// Falla
	float probabilidad = lcgrand(Falla);
	if (probabilidad <= 0.2)
	{
		transfer[_Tiempo] = sim_time + uniform(interarribo_falla_min, interarribo_falla_max, Falla);
		transfer[_Evento] = Falla;

		list_file(INCREASING, LIST_EVENT);
	}
}

void RutinaInicioJornada(void)
{
	recibir_llamado = true;

	// Arribo llamado
	transfer[_Tiempo] = sim_time + expon(interarribo_llamado, ArriboLlamado);
	transfer[_Evento] = ArriboLlamado;

	list_file(INCREASING, LIST_EVENT);

	// Fin jornada
	transfer[_Tiempo] = sim_time + fin_jornada;
	transfer[_Evento] = FinJornada;

	list_file(INCREASING, LIST_EVENT);

	// Falla
	float probabilidad = lcgrand(Falla);
	if (probabilidad <= 0.2)
	{
		transfer[_Tiempo] = sim_time + uniform(interarribo_falla_min, interarribo_falla_max, Falla);
		transfer[_Evento] = Falla;

		list_file(INCREASING, LIST_EVENT);
	}
}

void RutinaFinJornada(void)
{
	recibir_llamado = false;
	
	// Proximo inicio jornada
	transfer[_Tiempo] = sim_time + inicio_jornada;
	transfer[_Evento] = InicioJornada;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaArriboLlamado(void)
{
	if (list_size[Operador1] == 0 && descanso_operador1 == false)
	{
		sampst(sim_time - 0, DemoraEspera);
		OcuparOperador(Operador1);
	}
	else if (list_size[Operador2] == 0 && descanso_operador2 == false)
	{
		sampst(sim_time - 0, DemoraEspera);
		OcuparOperador(Operador2);
	}
	else if (list_size[Operador3] == 0 && descanso_operador3 == false)
	{
		sampst(sim_time - 0, DemoraEspera);
		OcuparOperador(Operador3);
	}
	else if (list_size[Operador4] == 0 && descanso_operador4 == false)
	{
		sampst(sim_time - 0, DemoraEspera);
		OcuparOperador(Operador4);
	}
	else
	{
		float probabilidad = lcgrand(14);
		if (probabilidad > 0.2 && probabilidad <= 0.4) // Espera poco
		{
			transfer[_PocaEspera] = true;
			list_file(LAST, Espera);

			// Generar cancelar espera
			transfer[_Tiempo] = sim_time + uniform(2, 3, FinEspera);
			transfer[_Evento] = FinEspera;
			transfer[5] = sim_time;
			list_file(INCREASING, LIST_EVENT);
		}
		else if (probabilidad > 0.4)
		{
			list_file(LAST, Espera);
		}
	}

	// Proximo arribo llamado
	if (recibir_llamado)
	{
		transfer[_Tiempo] = sim_time + expon(interarribo_llamado, ArriboLlamado);
		transfer[_Evento] = ArriboLlamado;
		list_file(INCREASING, LIST_EVENT);
	}
}

void OcuparOperador(int operador)
{
	transfer[_Tiempo] = sim_time;
	transfer[_Evento] = ArriboLlamado;
	transfer[_Operador] = operador;
	list_file(FIRST, operador);
	GenerarFinLlamado(operador);
}

void RutinaFinLlamado(void)
{
	int operador = transfer[_Operador];
	list_remove(FIRST, operador);

	sampst(sim_time - transfer[_Tiempo], TiempoAtencion);

	if (DescansoOperador(operador) == false && list_size[Espera] > 0)
	{
		list_remove(FIRST, Espera);
		sampst(sim_time - transfer[_Tiempo], DemoraEspera);
		float tiempo = transfer[_Tiempo];
		
		// Si el llamado es del 40% que espera poco, eliminar la cancelacion del llamado.
		if (transfer[_PocaEspera])
		{
			event_cancel(FinEspera);
			while (transfer[5] != tiempo)
			{
				list_file(FIRST, AuxEventos);
				event_cancel(FinEspera);
			}

			while (list_size[AuxEventos] > 0)
			{
				list_remove(FIRST, AuxEventos);
				list_file(INCREASING, LIST_EVENT);
			}
		}

		OcuparOperador(operador);
	}
}

bool DescansoOperador(int operador)
{
	switch (operador)
	{
		case 1:
			return descanso_operador1;
		case 2:
			return descanso_operador2;
		case 3:
			return descanso_operador3;
		case 4:
			return descanso_operador4;
	}
}

void GenerarFinLlamado(int operador)
{
	float probabilidad = lcgrand(FinLlamado);
	if (probabilidad <= 0.35)
	{
		transfer[_Tiempo] = sim_time + uniform(llamado_corto_min, llamado_corto_max, FinLlamado);
	}
	else
	{
		transfer[_Tiempo] = sim_time + expon(llamado_largo, FinLlamado);
	}
	transfer[_Evento] = FinLlamado;
	transfer[_Operador] = operador;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaDescanso(void)
{
	int operador = transfer[_Operador];

	ActualizarDescanso(operador, true);

	// Fin descanso
	transfer[_Tiempo] = sim_time + tiempo_descanso;
	transfer[_Evento] = FinDescanso;
	transfer[_Operador] = operador;

	list_file(INCREASING, LIST_EVENT);

	// Proximo descanso
	if (recibir_llamado)
	{
		transfer[_Tiempo] = sim_time + interarribo_descanso;
		transfer[_Evento] = Descanso;
		switch (operador)
		{
		case 1:
			transfer[_Operador] = Operador2;
			break;
		case 2:
			transfer[_Operador] = Operador3;
			break;
		case 3:
			transfer[_Operador] = Operador4;
			break;
		case 4:
			transfer[_Operador] = Operador1;
			break;
		}

		list_file(INCREASING, LIST_EVENT);
	}
}

void ActualizarDescanso(int operador, bool valor)
{
	switch (operador)
	{
	case 1:
		descanso_operador1 = valor;
		break;
	case 2:
		descanso_operador2 = valor;
		break;
	case 3:
		descanso_operador3 = valor;
		break;
	case 4:
		descanso_operador4 = valor;
		break;
	}
}

void RutinaFinDescanso(void)
{
	int operador = transfer[_Operador];

	ActualizarDescanso(operador, false);

	// Atender un llamado si hay en espera
	if (list_size[Espera] > 0)
	{
		list_remove(FIRST, Espera);
		sampst(sim_time - transfer[_Tiempo], DemoraEspera);
		OcuparOperador(operador);
	}
}

void RutinaFalla(void)
{
	falla++;

	if (list_size[Operador1] > 0)
	{
		list_remove(FIRST, Operador1);
	}
	if (list_size[Operador2] > 0)
	{
		list_remove(FIRST, Operador2);
	}
	if (list_size[Operador3] > 0)
	{
		list_remove(FIRST, Operador3);
	}
	if (list_size[Operador4] > 0)
	{
		list_remove(FIRST, Operador4);
	}

	while (list_size[Espera] > 0)
	{
		list_remove(FIRST, Espera);
	}

	event_cancel(FinJornada);
	int transcurrido = sim_time - transfer[_Tiempo];

	while (list_size[LIST_EVENT] > 1)
	{
		list_remove(FIRST, LIST_EVENT);
	}

	// Generar eventos iniciales
	// Arribo llamado
	transfer[_Tiempo] = sim_time + expon(interarribo_llamado, ArriboLlamado);
	transfer[_Evento] = ArriboLlamado;

	list_file(INCREASING, LIST_EVENT);

	// Fin de jornada
	transfer[_Tiempo] = sim_time + fin_jornada - transcurrido;
	transfer[_Evento] = FinJornada;

	list_file(INCREASING, LIST_EVENT);

	// Inicio descanso
	transfer[_Tiempo] = sim_time + interarribo_descanso;
	transfer[_Evento] = Descanso;
	transfer[_Operador] = 1;

	list_file(INCREASING, LIST_EVENT);
}

void RutinaFinEspera(void)
{
	float tiempo = transfer[5];

	list_remove(LAST, Espera);
	if (transfer[_Tiempo] != tiempo)
	{
		list_file(LAST, AuxEspera);
		list_remove(LAST, Espera);
	}
	while (list_size[AuxEspera] > 0) 
	{
		list_remove(LAST, AuxEspera);
		list_file(LAST, Espera);
	}
}

// Generar Reporte de Simulación
void Reporte(void)
{
	// Impresión en Pantalla
	printf("Estadisticos:\n\n");

	printf("Cantidad de llamados: %i\n", cantidad_llamados);
	// Demora media de las personas en espera, se consideran todos los llamados 
	// que estuvieron en la cola hayan sido atendidos o no.
	sampst(0, -DemoraEspera);
	printf("\nDemora media de las personas en espera: %.2f minutos\n", transfer[1]);

	// Número medio en la cola de llamados en espera.
	filest(DemoraEspera);
	printf("\nNumero medio de llamados en espera: %.2f\n", transfer[1]);
	
	// Demora promedio total desde que el cliente llama hasta que finaliza con su consulta.
	sampst(0, -TiempoAtencion);
	printf("\nDuracion media de los llamados: %.2f minutos\n", transfer[1]);

	// Cantidad de fallas ocurridas durante toda la simulación.
	printf("\nCantidad de fallas ocurridas: %i\n", falla);

	// Ocupación de cada uno de los operadores.
	filest(Operador1);
	printf("\nOcupacion del operador 1: %.2f %%\n", transfer[1] * 100);
	filest(Operador2);
	printf("\nOcupacion del operador 2: %.2f %%\n", transfer[1] * 100);
	filest(Operador3);
	printf("\nOcupacion del operador 3: %.2f %%\n", transfer[1] * 100);
	filest(Operador4);
	printf("\nOcupacion del operador 4: %.2f %%\n", transfer[1] * 100);
}