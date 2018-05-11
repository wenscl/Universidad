#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>

// Eventos
#define Falla				1
#define FinReparacion		2
#define InicioJornada		3
#define FinJornada			4
#define LlamarTecnico		5

//Colas y Listas
#define Maquina1			1
#define Maquina2			2
#define Maquina3			3
#define Maquina4			4
#define Tecnico1			5
#define Tecnico2			6
#define Tecnico3			7
#define OtroTecnico			8
#define Espera				9

// Sampst
#define DemoraEspera		1

// Posiciones de Transfer
#define _Tiempo				1
#define _Evento				2
#define _Maquina			3
#define	_Tecnico			4

// Variables
int interarribo_falla, reparacion_menor_min, reparacion_menor_max, reparacion_mayor_min, reparacion_mayor_max,
	inicio_jornada, fin_jornada, tiempo_simulacion, cantidad_fallas;
bool guardia;
float inactividad_maquina1, inactividad_maquina2, inactividad_maquina3, inactividad_maquina4,
	inactividad_maquina5, inactividad_maquina6, actividad_tecnico1, actividad_tecnico2, actividad_tecnico3,
	actividad_guardia;

// Rutinas
int main();
void Inicializacion(void);
void RutinaFalla(void);
void RutinaFinReparacion(void);
void RutinaInicioJornada(void);
void RutinaFinJornada(void);
void RutinaLlamarTecnico(void);
void Reporte(void);
void GenerarFinReparacion(int tecnico, float tiempo);

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
			case Falla:
				cantidad_fallas++;
				RutinaFalla();
				break;
			case FinReparacion:
				RutinaFinReparacion();
				break;
			case InicioJornada:
				RutinaInicioJornada();
				break;
			case FinJornada:
				RutinaFinJornada();
				break;
			case LlamarTecnico:
				RutinaLlamarTecnico();
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
	interarribo_falla = 480;
	reparacion_menor_min = 20;
	reparacion_menor_max = 40;
	reparacion_mayor_min = 90;
	reparacion_mayor_max = 150;
	inicio_jornada = 720;
	fin_jornada = 720;
	guardia = false;
	tiempo_simulacion = 48000;
	inactividad_maquina1, inactividad_maquina2, inactividad_maquina3, inactividad_maquina4, inactividad_maquina5, 
		inactividad_maquina6, actividad_tecnico1, actividad_tecnico2, actividad_tecnico3, actividad_guardia = 0;
	cantidad_fallas = 0;
	// Generar eventos iniciales
	
	// 6 fallas
	for (int i = 1; i < 7; i++)
	{
		transfer[_Tiempo] = sim_time + expon(interarribo_falla, Falla);
		transfer[_Evento] = Falla;
		transfer[_Maquina] = i;
		list_file(INCREASING, LIST_EVENT);
	}

	// Fin jornada
	transfer[_Tiempo] = sim_time + fin_jornada;
	transfer[_Evento] = FinJornada;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaFalla(void)
{
	int maquina = transfer[_Maquina];
	if (guardia)
	{
		if (list_size[Tecnico1] == 0)
		{
			list_file(LAST, Espera);
			transfer[_Tiempo] = sim_time + 30;
			transfer[_Evento] = LlamarTecnico;
			list_file(INCREASING, LIST_EVENT);
		}
		else
		{
			list_file(LAST, Espera);
		}
	}
	else
	{
		if (list_size[Tecnico1] == 0)
		{
			sampst(0, DemoraEspera);
			transfer[_Tecnico] = Tecnico1;
			list_file(FIRST, Tecnico1);
			GenerarFinReparacion(Tecnico1, sim_time);
		}
		else if (list_size[Tecnico2] == 0)
		{
			sampst(0, DemoraEspera);
			transfer[_Tecnico] = Tecnico2;
			list_file(FIRST, Tecnico2);
			GenerarFinReparacion(Tecnico2, sim_time);
		}
		else if (list_size[Tecnico3] == 0)
		{
			sampst(0, DemoraEspera);
			transfer[_Tecnico] = Tecnico3;
			list_file(FIRST, Tecnico3);
			GenerarFinReparacion(Tecnico3, sim_time);
		}
		else if (list_size[Espera] > 0 && list_size[OtroTecnico] == 0)
		{
			sampst(0, DemoraEspera);
			transfer[_Tecnico] = OtroTecnico;
			list_file(FIRST, OtroTecnico);
			GenerarFinReparacion(OtroTecnico, sim_time);
		}
		else
		{
			list_file(LAST, Espera);
		}
	}

	// Siguiente falla
	transfer[_Tiempo] = sim_time + expon(interarribo_falla, Falla);
	transfer[_Evento] = Falla;
	transfer[_Maquina] = maquina;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaFinReparacion(void)
{
	int tecnico = transfer[_Tecnico];
	list_remove(FIRST, tecnico);
	
	int maquina = transfer[_Maquina];
	switch (maquina)
	{
	case 1:
		inactividad_maquina1 += sim_time - transfer[_Tiempo];
		break;
	case 2:
		inactividad_maquina2 += sim_time - transfer[_Tiempo];
		break;
	case 3:
		inactividad_maquina3 += sim_time - transfer[_Tiempo];
		break;
	case 4:
		inactividad_maquina4 += sim_time - transfer[_Tiempo];
		break;
	case 5:
		inactividad_maquina5 += sim_time - transfer[_Tiempo];
		break;
	case 6:
		inactividad_maquina6 += sim_time - transfer[_Tiempo];
		break;
	}

	if (tecnico != OtroTecnico && list_size[Espera] > 0)
	{
		switch (tecnico)
		{
		case 5:
			if (guardia)
			{
				actividad_guardia += sim_time - transfer[_Tiempo];
			}
			else
			{
				actividad_tecnico1 += sim_time - transfer[_Tiempo];
			}
			break;
		case 6:
			actividad_tecnico2 += sim_time - transfer[_Tiempo];
			break;
		case 7:
			actividad_tecnico3 += sim_time - transfer[_Tiempo];
			break;
		}

		if (guardia == false)
		{
			list_remove(FIRST, Espera);
			sampst(sim_time - transfer[_Tiempo], DemoraEspera);
			transfer[_Tiempo] = sim_time;
			transfer[_Tecnico] = tecnico;
			list_file(FIRST, tecnico);
			GenerarFinReparacion(tecnico, sim_time);
		}
	}
}

void RutinaInicioJornada(void)
{
	guardia = false;

	// Fin jornada
	transfer[_Tiempo] = sim_time + fin_jornada;
	transfer[_Evento] = FinJornada;
	list_file(INCREASING, LIST_EVENT);

	if (list_size[Espera] > 0)
	{
		list_remove(FIRST, Espera);
		sampst(sim_time - transfer[_Tiempo], DemoraEspera);
		transfer[_Tiempo] = sim_time;
		transfer[_Tecnico] = Tecnico2;
		list_file(FIRST, Tecnico2);
		GenerarFinReparacion(Tecnico2, sim_time);

		if (list_size[Espera] > 0)
		{
			list_remove(FIRST, Espera);
			sampst(sim_time - transfer[_Tiempo], DemoraEspera);
			transfer[_Tiempo] = sim_time;
			transfer[_Tecnico] = Tecnico3;
			list_file(FIRST, Tecnico3);
			GenerarFinReparacion(Tecnico3, sim_time);
		}
	}
}

void RutinaFinJornada(void)
{
	guardia = true;

	// Inicio jornada
	transfer[_Tiempo] = sim_time + inicio_jornada;
	transfer[_Evento] = InicioJornada;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaLlamarTecnico(void)
{
	if (list_size[Tecnico1] == 0)
	{
		list_remove(FIRST, Espera);
		sampst(30, DemoraEspera);
		transfer[_Tiempo] = sim_time;
		transfer[_Tecnico] = Tecnico1;
		list_file(FIRST, Tecnico1);
		GenerarFinReparacion(Tecnico1, sim_time);
	}
}

void GenerarFinReparacion(int tecnico, float tiempo)
{
	float probabilidad = lcgrand(Falla);
	if (probabilidad <= 0.30)
	{
		transfer[_Tiempo] = tiempo + uniform(reparacion_menor_min, reparacion_menor_max, FinReparacion);
	}
	else
	{
		transfer[_Tiempo] = tiempo + uniform(reparacion_mayor_min, reparacion_mayor_max, FinReparacion);
	}
	transfer[_Evento] = FinReparacion;
	transfer[_Tecnico] = tecnico;
	list_file(INCREASING, LIST_EVENT);
}

// Generar Reporte de Simulación
void Reporte(void)
{
	// Impresión en Pantalla
	printf("Estadisticos:\n");

	printf("\nCantidad de fallas: %i\n", cantidad_fallas);

	// -Utilización media y máxima del Técnico 1.
	filest(Tecnico1);
	printf("\nUtilizacion media del Tecnico 1: %.2f %%\n", transfer[1] * 100);
	printf("\nUtilizacion maxima del Tecnico 1: %.2f %%\n", transfer[3] * 100);

	// - Demora media, máxima, mínima de las máquinas en espera para comenzar a ser reparadas.
	sampst(0, -DemoraEspera);
	printf("\nTiempo minimo de espera: %.2f minutos\n", transfer[4]);
	printf("\nTiempo medio de espera: %.2f minutos\n", transfer[1]);
	printf("\nTiempo maximo de espera: %.2f minutos\n", transfer[3]);

	// - Número medio de máquinas en cola de espera.
	filest(DemoraEspera);
	printf("\nNumero medio de maquinas en espera: %.2f\n", transfer[1]);

	// - Costo total del sistema de reparación en las 800 hs.simuladas considerando el costo de
	// inactividad de las máquinas y el costo de los 3 técnicos estables.
	float inactividad = inactividad_maquina1 * 120 / 60 + inactividad_maquina2 * 120 / 60 + inactividad_maquina3 * 120 / 60
		+ inactividad_maquina4 * 120 / 60 + inactividad_maquina5 * 120 / 60 + inactividad_maquina6 * 120 / 60;
	float tecnicos = actividad_tecnico1 * 40 / 60 + actividad_tecnico2 * 40 / 60 + actividad_tecnico3 * 40 / 60
		+ actividad_guardia * 90 / 60;
	printf("\nCosto total del sistema de reparacion: $%.2f\n", inactividad + tecnicos);
}
