#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>

// Eventos
#define ArriboClienteAC			1
#define FinAtencionAlCliente	2
#define ArriboCaja				3
#define FinAtencionCaja			4
#define InicioJornadaLaboral	5
#define FinJornadaLaboral		6

// Colas y Listas
#define Representante1			1
#define Representante2			2
#define Caja1					3
#define Caja2					4
#define Caja3					5
#define ColaAtencion			6
#define ColaCaja				7
#define AuxVolverAC				9
#define ClientesConsulta		8	// Para calcular el numero medio de clientes que vienen por primera vez
#define ClientesBanco			9	// Para calcular el numero medio de clientes en el banco

// Sampst
#define DemoraCreditosCaja		1

// TipoCliente
#define Consulta				1
#define Credito					2
#define Caja					3

// Transfers
#define _Tiempo					1
#define _TipoEvento				2
#define _TipoCliente			3
#define _Representante			4
#define _Caja					5
#define _VolverAC				6

// Variables
float porcentaje_tipo_cliente, interarribo_cliente_consulta, interarribo_cliente_credito, atencion_consulta_min, atencion_consulta_max, 
	atencion_credito_min, atencion_credito_max, porcentaje_credito_caja, atencion_credito_constante, interarribo_caja,
	atencion_caja_min, atencion_caja_max, probabilidad;
int fin_jornada, inicio_jornada, fin_simulacion, creditos_otorgados, tipo_cliente, representante, caja, cantidad_clientes_AC,
	cantidad_clientes_caja;
bool atender, bandera, volver_ac;

// Rutinas
int main();
void Inicializacion(void);
void RutinaArriboClienteAC(void);
void RutinaFinAtencionAlCliente(void);
void RutinaArriboCaja(void);
void RutinaFinAtencionCaja(void);
void RutinaInicioJornadaLaboral(void);
void RutinaFinJornadaLaboral(void);
void GenerarArriboClienteAC(void);
void GenerarArriboClienteCaja(void);
void GenerarFinAtencionAlCliente(int tipo_cliente, int representante, bool paso_caja);
void Reporte(void);

//Funcion Principal
int main()  
{
	// Inicializar SimLib
	init_simlib();

	// Rutina Inicializar
	Inicializacion();

	// Comienzo Simulacion
	while (sim_time <= fin_simulacion)
	{
		timing();

		// Determinar tipo de evento y llamar a su rutina
		switch(next_event_type)
		{
			case InicioJornadaLaboral:
				RutinaInicioJornadaLaboral();
				break;
			case FinJornadaLaboral:
				RutinaFinJornadaLaboral();
				break;
			case ArriboClienteAC:
				cantidad_clientes_AC++;
				RutinaArriboClienteAC();
				break;
			case FinAtencionAlCliente:
				RutinaFinAtencionAlCliente();
				break;
			case ArriboCaja:
				cantidad_clientes_caja++;
				RutinaArriboCaja();
				break;
			case FinAtencionCaja:
				RutinaFinAtencionCaja();
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
	porcentaje_tipo_cliente = 0.6;
	interarribo_cliente_consulta = 30; 
	interarribo_cliente_credito = 90;
	atencion_consulta_min = 20;
	atencion_consulta_max = 40; 
	atencion_credito_min = 30; 
	atencion_credito_max = 60; 
	porcentaje_credito_caja = 0.5; 
	atencion_credito_constante = 5; 
	interarribo_caja = 3.5; 
	atencion_caja_min = 3; 
	atencion_caja_max = 10;
	fin_jornada = 300;
	inicio_jornada = 1140;
	fin_simulacion = 7200;
	creditos_otorgados = 0;
	probabilidad = 0;
	tipo_cliente = 0;
	atender = false;
	representante = 0;
	caja = 0;
	bandera = false;
	volver_ac = false;
	cantidad_clientes_AC = 0;
	cantidad_clientes_caja = 0;

	// Generar eventos iniciales
	transfer[_Tiempo] = sim_time;
	transfer[_TipoEvento] = InicioJornadaLaboral;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaInicioJornadaLaboral(void)
{
	atender = true;

	// Generar primer arribo cliente consulta/credito
	GenerarArriboClienteAC();

	// Generar primer arribo cliente caja
	GenerarArriboClienteCaja();

	// Generar porximo fin jornada laboral
	transfer[_Tiempo] = sim_time + fin_jornada;
	transfer[_TipoEvento] = FinJornadaLaboral;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaFinJornadaLaboral(void)
{
	atender = false;

	// Generar proximo inicio jornada laboral
	transfer[_Tiempo] = sim_time + inicio_jornada;
	transfer[_TipoEvento] = InicioJornadaLaboral;
	list_file(INCREASING, LIST_EVENT);
}

void RutinaArriboClienteAC(void)
{
	tipo_cliente = transfer[_TipoCliente];
	if (list_size[Representante1] == 0)		// Representante 1 desocupado
	{
		transfer[_Representante] = Representante1;
		list_file(FIRST, Representante1);

		// Generar fin atencion al cliente
		GenerarFinAtencionAlCliente(tipo_cliente, Representante1, false);
	}
	else if (list_size[Representante2] == 0)// Representante 2 desocupado
	{
		transfer[_Representante] = Representante2;
		list_file(FIRST, Representante2);

		// Generar fin atencion al cliente
		GenerarFinAtencionAlCliente(tipo_cliente, Representante2, false);
	}
	else // Poner en espera
	{
		tipo_cliente = transfer[_TipoCliente];
		transfer[_VolverAC] = false;
		list_file(LAST, ColaAtencion);
		if (tipo_cliente == Consulta)
		{
			list_file(FIRST, ClientesConsulta);
		}
	}

	transfer[_Tiempo] = sim_time;
	list_file(FIRST, ClientesBanco);
	
	// Generar proximo arribo cliente consulta/credito
	if (atender)
	{
		GenerarArriboClienteAC();
	}
}

void SepararColaAC(void)
{
	if (list_size[ColaAtencion] > 0)
	{
		list_remove(FIRST, ColaAtencion);
		while (transfer[_VolverAC])
		{
			bandera = false;
			list_file(LAST, AuxVolverAC);
			if (list_size[ColaAtencion] > 0)
			{
				list_remove(FIRST, ColaAtencion);
				bandera = true;
			}
			if (bandera == false)
			{
				return;
			}
		}
	}
	if (bandera)
	{
		list_file(FIRST, ColaAtencion);
	}
}

void JuntarColaAC(void)
{
	while (list_size[AuxVolverAC] > 0)
	{
		list_remove(LAST, AuxVolverAC);
		list_file(FIRST, ColaAtencion);
	}
}

void RutinaFinAtencionAlCliente(void)
{
	representante = transfer[_Representante];
	list_remove(FIRST, representante);

	// Poner otro cliente
	if (list_size[ColaAtencion] > 0)
	{
		list_remove(FIRST, ColaAtencion);
		transfer[_Tiempo] = sim_time;
		tipo_cliente = transfer[_TipoCliente];
		volver_ac = transfer[_VolverAC];
		list_file(FIRST, representante);

		if (tipo_cliente == Consulta)
		{
			list_remove(FIRST, ClientesConsulta);
		}

		// Generar fin atencion al cliente
		GenerarFinAtencionAlCliente(tipo_cliente, representante, volver_ac);
	}
}

void RutinaArriboCaja(void)
{
	if (list_size[Caja1] == 0)		// Caja 1 desocupada
	{
		transfer[_Caja] = Caja1;
		list_file(FIRST, Caja1);
	}
	else if (list_size[Caja2] == 0)	// Caja 2 desocupada
	{
		transfer[_Caja] = Caja2;
		list_file(FIRST, Caja2);
	}
	else if (list_size[Caja3] == 0)	// Caja 3 desocupada
	{
		transfer[_Caja] = Caja3;
		list_file(FIRST, Caja3);
	}
	else // Poner en espera
	{
		list_file(LAST, ColaCaja);
	}

	// Generar proximo arribo cliente caja
	if (atender)
	{
		GenerarArriboClienteCaja();
	}
}

void RutinaFinAtencionCaja(void)
{
	caja = transfer[_Caja];
	list_remove(FIRST, caja);
	if (transfer[_TipoCliente] == Credito)	// El cliente tiene que volver a AC
	{
		creditos_otorgados++;
		representante = transfer[_Representante];
		if (list_size[representante] == 0)	// Representante que lo atendio esta desocupado
		{
			list_file(FIRST, representante);

			// Generar fin de atencion al cliente
			GenerarFinAtencionAlCliente(Credito, representante, true);
		}
		else
		{
			// Representante ocupado.. Ponerlo en cola
			SepararColaAC();
			if (list_size[AuxVolverAC] == 0)
			{
				list_file(FIRST, ColaAtencion);
			}
			else
			{
				list_file(LAST, AuxVolverAC);
			}
			JuntarColaAC();
		}
	}

	// Poner otro cliente
	if (list_size[ColaCaja] > 0)
	{
		list_remove(FIRST, ColaCaja);
		tipo_cliente = transfer[_TipoCliente];
		if (tipo_cliente == Credito)
		{
			representante = transfer[_Representante];
			volver_ac = transfer[_VolverAC];
			sampst(sim_time - transfer[_Tiempo], DemoraCreditosCaja);
		}
		transfer[_Tiempo] = sim_time;										// VER ESTOOOOOOOOO
		list_file(FIRST, caja);
		
		// Generar el fin de atencion caja
		transfer[_Tiempo] = sim_time + uniform(atencion_caja_min, atencion_caja_max, FinAtencionCaja);
		transfer[_TipoEvento] = FinAtencionCaja;
		transfer[_Caja] = caja;
		if (tipo_cliente == Credito)
		{
			transfer[_Representante] = representante;
			transfer[_VolverAC] = volver_ac;
		}
		list_file(INCREASING, LIST_EVENT);
	}
}

void GenerarArriboClienteAC(void)
{
	probabilidad = lcgrand(ArriboClienteAC);
	if (probabilidad <= porcentaje_tipo_cliente)
	{
		transfer[_Tiempo] = sim_time + expon(interarribo_cliente_consulta, ArriboClienteAC);
		transfer[_TipoCliente] = Consulta;
	}
	else
	{
		transfer[_Tiempo] = sim_time + expon(interarribo_cliente_credito, ArriboClienteAC);
		transfer[_TipoCliente] = Credito;
	}
	transfer[_TipoEvento] = ArriboClienteAC;
	list_file(INCREASING, LIST_EVENT);
}

void GenerarArriboClienteCaja(void)
{
	transfer[_Tiempo] = sim_time + expon(interarribo_caja, ArriboCaja);
	transfer[_TipoEvento] = ArriboCaja;
	transfer[_TipoCliente] = Caja;
	list_file(INCREASING, LIST_EVENT);
}

void GenerarFinAtencionAlCliente(int tipo_cliente, int representante, bool paso_caja)
{
	transfer[_TipoCliente] = tipo_cliente;
	if (paso_caja)	// Cliente de credito que ya paso por caja
	{
		transfer[_Tiempo] = sim_time + atencion_credito_constante;
		transfer[_TipoEvento] = FinAtencionAlCliente;
		transfer[_Representante] = representante;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		if (tipo_cliente == Consulta)	// Cliente que consulta
		{
			transfer[_Tiempo] = sim_time + uniform(atencion_consulta_min, atencion_consulta_max, FinAtencionAlCliente);
			transfer[_TipoEvento] = FinAtencionAlCliente;
			transfer[_Representante] = representante;
			list_file(INCREASING, LIST_EVENT);
		}
		else
		{
			
			probabilidad = lcgrand(14);
			if (probabilidad <= porcentaje_credito_caja)	// Cliente de credito que pasa por caja
			{
				// Poner en Caja
				transfer[_Tiempo] = sim_time;
				transfer[_TipoEvento] = ArriboCaja;
				transfer[_Representante] = representante;
				transfer[_VolverAC] = true;
				if (list_size[Caja1] == 0)
				{
					transfer[_Caja] = Caja1;
					sampst(0, DemoraCreditosCaja);
					list_file(FIRST, Caja1);
				}
				else if (list_size[Caja2] == 0)
				{
					transfer[_Caja] = Caja2;
					sampst(0, DemoraCreditosCaja);
					list_file(FIRST, Caja2);
				}
				else if (list_size[Caja3] == 0)
				{
					transfer[_Caja] = Caja3;
					sampst(0, DemoraCreditosCaja);
					list_file(FIRST, Caja3);
				}
				else
				{
					list_file(LAST, ColaCaja);
				}
			}
			else	// Cliente de credito que no pasa por caja
			{
				transfer[_Tiempo] = sim_time + uniform(atencion_credito_min, atencion_credito_max, FinAtencionAlCliente);
				transfer[_TipoEvento] = FinAtencionAlCliente;
				transfer[_Representante] = representante;
				list_file(INCREASING, LIST_EVENT);
			}
		}
	}
}

// Generar Reporte de Simulación
void Reporte(void)
{
	printf("ESTADISTICOS\n\n");

	// Cantidad de clientes atendidos
	printf("Cantidad de clientes atendidos en Atencion al Cliente: %i\n\n", cantidad_clientes_AC);
	printf("Cantidad de clientes atendidos en Cajas: %i\n\n", cantidad_clientes_caja);

	// Demora media de los clientes de Créditos en Cola de Cajas.
	sampst(0, -DemoraCreditosCaja);
	printf("Demora media de los clientes de credito en la cola de cajas: %.2f minutos\n\n", transfer[1]);
	
	// Número medio de clientes en la Cola de Cajas.
	filest(ColaCaja);
	printf("Numero medio de clientes en la cola de cajas: %.2f\n\n", transfer[1]);
	
	// Número medio de clientes que vienen por primera vez en la Cola de Espera del área de Créditos.
	filest(ClientesConsulta);
	printf("Numero medio de clientes que vienen por primera vez en la cola de espera: %.2f\n\n", transfer[1]);

	// Utilización promedio de los Representantes de Atención al Cliente.
	filest(Representante1);
	printf("Utilizacion promedio del representante 1: %.2f%%\n\n", transfer[1] * 100);
	filest(Representante2);
	printf("Utilizacion promedio del representante 2: %.2f%%\n\n", transfer[1] * 100);
	
	// Cantidad de Créditos otorgados durante la Simulación.
	printf("Cantidad de creditos otorgados: %.2f\n\n", creditos_otorgados);

	// Número medio de clientes en el banco.
	filest(ClientesBanco);
	printf("Numero medio de clientes en el banco: %.2f\n\n", transfer[1]);
}