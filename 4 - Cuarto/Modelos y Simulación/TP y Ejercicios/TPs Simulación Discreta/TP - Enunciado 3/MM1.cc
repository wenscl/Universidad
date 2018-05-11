/* Modelo MM1 - Un Servidor, Una Cola  */


#include "simlib.c"
#include <stdio.h>
#include <stdlib.h> 

//Eventos
#define ArriboPiezas			1
#define FinLimpieza				2
#define FinLubricacion			3
#define FinRevision				4 
#define FinEnsamblado			5

//Colas
#define ColaEtapa1				1
#define ColaEtapa2PiezaA		2
#define ColaEtapa2PiezaB		3
#define ColaEtapa3PiezaA		4
#define ColaEtapa3PiezaB		5
#define	MaquinaLimpieza			6
#define	MaquinaLubricacion		7
#define	MaquinaRevision			8
#define	MaquinaEnsamblado		9
#define PiezaEliminada			10

#define DemoraCola_PiezaA		1
#define DemoraCola_PiezaB		2
#define Permanencia				3

// Declaracion de variables
float interarribos_min, interarribos_max, servicio_limpieza, servicio_lubricacion, servicio_revision_min, servicio_revision_max, servicio_ensamblado;
int tiempo_fin, tipo_pieza, piezas_rechazadas, anomalias, terminados, cant_piezas, cant_piezas_atendidas;

// Declaracion de Funciones
void Inicializar(void);
void Rutina_ArriboPiezas(void);
void Rutina_FinLimpieza(void);
void Rutina_FinLubricacion(void);
void Rutina_FinRevision(void);
void Rutina_FinEnsamblado(void);
void Reporte(void);


// CONTROLAR LOS SAMPTS CON 0


int main()
{
	// Inicializar Simlib
	init_simlib();

	// Inicializar el Sistema
	Inicializar();

	while (sim_time < tiempo_fin)
	{
		// Determinar proximo Evento
		timing();
		switch (next_event_type)
		{
		case ArriboPiezas:
			cant_piezas++;
			Rutina_ArriboPiezas();
			break;
		case FinLimpieza:
			Rutina_FinLimpieza();
			break;
		case FinLubricacion:
			Rutina_FinLubricacion();
			break;
		case FinRevision:
			Rutina_FinRevision();
			break;
		case FinEnsamblado:
			Rutina_FinEnsamblado();
			cant_piezas_atendidas++;
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
	tiempo_fin = 21600;
	interarribos_min = 1;
	interarribos_max = 2.5;
	servicio_limpieza = 2.8;
	servicio_lubricacion = 3.5;
	servicio_revision_min = 3;
	servicio_revision_max = 5;
	servicio_ensamblado = 3.1;
	piezas_rechazadas = 0;
	anomalias = 0;
	terminados = 0;
	cant_piezas = 0;
	cant_piezas_atendidas = 0;

	// Cargar la lista de eventos con los eventos que inicializan la simulacion
	// A = 1, B = 2
	for (int i = 0; i < 2; i++)
	{
		transfer[1] = sim_time + uniform(interarribos_min, interarribos_max, ArriboPiezas);
		transfer[2] = ArriboPiezas;
		transfer[3] = i + 1;
		list_file(INCREASING, LIST_EVENT);
	}
}

void Rutina_ArriboPiezas(void)
{
	if (list_size[MaquinaLimpieza] == 0)
	{
		tipo_pieza = transfer[3];
		sampst(0, tipo_pieza);
		list_file(LAST, MaquinaLimpieza);

		// Generar fin de la etapa Limpieza
		transfer[1] = sim_time + servicio_limpieza;
		transfer[2] = FinLimpieza;
		transfer[3] = tipo_pieza;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		list_file(LAST, ColaEtapa1);
	}
	
	// Generar proximo arribo de pieza
	transfer[1] = sim_time + uniform(interarribos_min, interarribos_max, ArriboPiezas);
	transfer[2] = ArriboPiezas;
	float pieza = lcgrand(15);
	if (pieza < 0.5)
		transfer[3] = 1;
	else
		transfer[3] = 2;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_FinLimpieza(void)
{
	list_remove(FIRST, MaquinaLimpieza);
	sampst(sim_time - transfer[1], Permanencia);
	transfer[1] = sim_time;
	tipo_pieza = transfer[3];
	if (tipo_pieza == 1)
	{
		if (list_size[MaquinaLubricacion] == 0)
		{
			sampst(0, tipo_pieza);
			list_file(FIRST, MaquinaLubricacion);

			// Determinar el Fin de la etapa Lubricacion
			transfer[1] = sim_time + expon(servicio_lubricacion, FinLubricacion);
			transfer[2] = FinLubricacion;
			transfer[3] = tipo_pieza;
			list_file(INCREASING, LIST_EVENT);
		}
		else
		{
			list_file(LAST, ColaEtapa2PiezaA);
		}
	}
	else
	{
		if (list_size[MaquinaRevision] == 0)
		{
			sampst(0, tipo_pieza);
			list_file(FIRST, MaquinaRevision);

			// Determinar el Fin de la etapa Revision
			transfer[1] = sim_time + uniform(servicio_revision_min, servicio_revision_max, FinRevision);
			transfer[2] = FinRevision;
			transfer[3] = tipo_pieza;
			list_file(INCREASING, LIST_EVENT);
		}
		else
		{
			list_file(LAST, ColaEtapa2PiezaB);
		}
	}

	if (list_size[ColaEtapa1] > 0)
	{
		list_remove(FIRST, ColaEtapa1);
		tipo_pieza = transfer[3];
		sampst(sim_time - transfer[1], tipo_pieza);
		transfer[1] = sim_time;
		list_file(FIRST, MaquinaLimpieza);

		//Determinar el Fin de la etapa Limpieza
		transfer[1] = sim_time + servicio_limpieza;
		transfer[2] = FinLimpieza;
		transfer[3] = tipo_pieza;
		list_file(INCREASING, LIST_EVENT);
	}
}

void Rutina_FinLubricacion(void)
{
	list_remove(FIRST, MaquinaLubricacion);
	sampst(sim_time - transfer[1], Permanencia);
	transfer[1] = sim_time;
	if (list_size[MaquinaEnsamblado] == 0 && list_size[ColaEtapa3PiezaB] > 0)
	{
		list_file(FIRST, MaquinaEnsamblado);
		list_remove(FIRST, ColaEtapa3PiezaB);
		sampst(sim_time - transfer[1], DemoraCola_PiezaB);
		transfer[1] = sim_time;
		list_file(LAST, MaquinaEnsamblado);

		//Determinar el Fin de la etapa Ensamblado
		transfer[1] = sim_time + expon(servicio_ensamblado, FinEnsamblado);
		transfer[2] = FinEnsamblado;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		list_file(LAST, ColaEtapa3PiezaA);
	}

	if (list_size[ColaEtapa2PiezaA] > 0)
	{
		list_remove(FIRST, ColaEtapa2PiezaA);
		sampst(sim_time - transfer[1], DemoraCola_PiezaA);
		transfer[1] = sim_time;
		list_file(FIRST, MaquinaLubricacion);

		// Determinar el Fin de la etapa Lubricacion
		transfer[1] = sim_time + expon(servicio_lubricacion, FinLubricacion);
		transfer[2] = FinLubricacion;
		transfer[3] = 1;
		list_file(INCREASING, LIST_EVENT);
	}
}

void Rutina_FinRevision(void)
{
	// Probabilidad de falla
	float falla = lcgrand(15);
	list_remove(FIRST, MaquinaRevision);
	sampst(sim_time - transfer[1], Permanencia);
	if (falla <= 0.05)
	{
		list_file(LAST, ColaEtapa1);
		piezas_rechazadas++;
	}
	else
	{
		if (list_size[MaquinaEnsamblado] == 0 && list_size[ColaEtapa3PiezaA] > 0)
		{
			list_file(LAST, MaquinaEnsamblado);
			list_remove(FIRST, ColaEtapa3PiezaA);
			sampst(sim_time - transfer[1], DemoraCola_PiezaA);
			transfer[1] = sim_time;
			list_file(FIRST, MaquinaEnsamblado);
			//Determinar el Fin de la etapa Ensamblado
			transfer[1] = sim_time + expon(servicio_ensamblado, FinEnsamblado);
			transfer[2] = FinEnsamblado;
			list_file(INCREASING, LIST_EVENT);
		}
		else
		{
			list_file(LAST, ColaEtapa3PiezaB);
		}
	}

	if (list_size[ColaEtapa2PiezaB] > 0)
	{
		list_remove(FIRST, ColaEtapa2PiezaB);
		sampst(sim_time - transfer[1], DemoraCola_PiezaB);
		transfer[1] = sim_time;
		list_file(FIRST, MaquinaRevision);
		//Determinar el Fin de la etapa Revision
		transfer[1] = sim_time + uniform(servicio_revision_min, servicio_revision_max, FinRevision);
		transfer[2] = FinRevision;
		transfer[3] = 2;
		list_file(INCREASING, LIST_EVENT);
	}
}

void Rutina_FinEnsamblado(void)
{
	// Probabilidad de anomalias
	float falla = lcgrand(15);
	if (falla <= 0.04)
	{
		list_remove(FIRST, MaquinaEnsamblado);
		sampst(sim_time - transfer[1], Permanencia);
		list_file(LAST, ColaEtapa1);
		list_remove(LAST, MaquinaEnsamblado);
		sampst(sim_time - transfer[1], Permanencia);
		list_file(LAST, ColaEtapa1);
		anomalias++;
	}
	else
	{
		list_remove(FIRST, MaquinaEnsamblado);
		sampst(sim_time - transfer[1], Permanencia);
		list_remove(LAST, MaquinaEnsamblado);
		sampst(sim_time - transfer[1], Permanencia);
	}

	if (list_size[ColaEtapa3PiezaA] > 0 && list_size[ColaEtapa3PiezaB] > 0)
	{
		list_remove(FIRST, ColaEtapa3PiezaA);
		sampst(sim_time - transfer[1], DemoraCola_PiezaA);
		transfer[1] = sim_time;
		list_file(FIRST, MaquinaEnsamblado);
		list_remove(FIRST, ColaEtapa3PiezaB);
		sampst(sim_time - transfer[1], DemoraCola_PiezaB);
		transfer[1] = sim_time;
		list_file(LAST, MaquinaEnsamblado);
		//Determinar el Fin de la etapa Ensamblado
		transfer[1] = sim_time + expon(servicio_ensamblado, FinEnsamblado);
		transfer[2] = FinEnsamblado;
		list_file(INCREASING, LIST_EVENT);
	}
}

void Reporte(void)
{
	printf("ESTADISTICAS\n");
	printf("\nCantidad de piezas generadas: %i \n", cant_piezas);
	printf("Cantidad de piezas atendidas: %i \n", cant_piezas_atendidas);

	filest(MaquinaLimpieza);
	printf("\nUtilizacion de la maquina de Limpieza: %.1f por ciento \n ", transfer[1] * 100);
	filest(MaquinaLubricacion);
	printf("\nUtilizacion de la maquina de Lubricacion: %.1f por ciento \n ", transfer[1] * 100);
	filest(MaquinaRevision);
	printf("\nUtilizacion de la maquina de Revision: %.1f por ciento \n ", transfer[1] * 100);
	filest(MaquinaEnsamblado);
	printf("\nUtilizacion de la maquina de Ensamblado: %.1f por ciento \n ", transfer[1] / 2 * 100);

	sampst(0, -DemoraCola_PiezaA);
	printf("\nDemora Media de espera de las piezas A: %.3f \n ", transfer[1]);
	sampst(0, -DemoraCola_PiezaB);
	printf("\nDemora Media de espera de las piezas B: %.3f \n ", transfer[1]);

	sampst(0, -Permanencia);
	printf("\nTiempo medio de permanencia de las piezas en el sistema: %.3f \n ", transfer[1]);

	printf("\nCantidad de piezas B rechazadas en la etapa de revision: %i \n ", piezas_rechazadas);

	printf("\nCantidad de productos que presentaron anomalias en la etapa de ensamblado: %i \n ", anomalias);
}