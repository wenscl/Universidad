/* Modelo MM1 - Un Servidor, Una Cola  */


#include "simlib.c"
#include <stdio.h>
#include <stdlib.h> 

//Eventos
#define PedidoEstacion    1 // Estacion pide red 
#define PedidoServidor    2 // Servidor pide red 
#define FinPedido         3 // 
#define Falla	          4 // Falla general

//Colas
#define Red               1 // Red
#define Pedidos			  2 // Cola pedidos de ambos
#define list_aux		  3
#define ColaServPrioridad 4
#define ColaServidor	  5
#define MediaEsperaServ	  6 // Para calcular la cantidad media de pedidos de servidor en espera
#define Red_aux			  7
#define	event_aux		  8

#define Demora_estacion1  1
#define Demora_estacion2  2
#define Demora_estacion3  3
#define Demora_estacion4  4
#define Demora_estacion5  5
#define Demora_estacion6  6

// Declaracion de variables
float media_interarribos_estacion, media_interarribos_servidor, media_servicio_estacion, media_servicio_servidor, 
	media_falla_min, media_falla_max, probabilidad, tiempo_red, tipo_pedido, tiempo_utilizacion;
int tiempo_fin, nro_estacion, pedidos_desplazados, falla, prioridad, cant_estacion, cant_servidor;
bool RedDisponible, bandera;

// Declaracion de Funciones
void Inicializar(void);
void Rutina_PedidoEstacion(void);
void Rutina_PedidoServidor(void);
void Rutina_FinPedido(void);
void Rutina_Falla(void);
void Reporte(void);

int main()
{

	// Inicializar Simlib
	init_simlib();

	// Inicializar el Sistema
	Inicializar();

	// borrar 
	cant_estacion = 0;
	cant_servidor = 0; 

	while (sim_time < tiempo_fin)
	{
		// Determinar proximo Evento
		timing();
		switch (next_event_type)
		{
		case PedidoEstacion:
			cant_estacion++;							// borrar
			Rutina_PedidoEstacion();
			break;
		case PedidoServidor:
			cant_servidor++;							// borrar
			Rutina_PedidoServidor();
			break;
		case FinPedido:
			Rutina_FinPedido();
			break;
		case Falla:
			Rutina_Falla();
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
	tiempo_fin = 86400;
	media_interarribos_estacion = 1.2;
	media_servicio_estacion = 3.7;
	media_interarribos_servidor = 3.7;
	media_servicio_servidor = 2.4;
	media_falla_min = 10800;
	media_falla_max = 14400;
	RedDisponible = true;
	pedidos_desplazados = 0;
	falla = 0;
	prioridad = 0;
	tiempo_red = 0;
	probabilidad = 0;
	tipo_pedido = 0;
	tiempo_utilizacion = 0;
	bandera = 0;

	// Cargar la lista de eventos con los eventos que inicializan la simulacion
	for (int i = 0; i < 6; i++)
	{
		transfer[1] = sim_time + expon(media_interarribos_estacion, PedidoEstacion);
		transfer[2] = PedidoEstacion;
		transfer[3] = i + 1;
		list_file(INCREASING, LIST_EVENT);
	}

	transfer[1] = sim_time + expon(media_interarribos_servidor, PedidoServidor);
	transfer[2] = PedidoServidor;
	list_file(INCREASING, LIST_EVENT);

	transfer[1] = sim_time + uniform(media_falla_min, media_falla_max, Falla);
	transfer[2] = Falla;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_PedidoEstacion(void)
{
	nro_estacion = transfer[3];
	RedDisponible = true;
	if (list_size[Red] > 0)
	{
		list_remove(FIRST, Red);
		tipo_pedido = transfer[2];
		prioridad = transfer[3];
		list_file(FIRST, Red);
		switch (list_size[Red])
		{
			case 1:
				if (tipo_pedido == PedidoServidor && prioridad == 1)
				{
					RedDisponible = false;
				}
				break;
			case 2:
				if (tipo_pedido == PedidoServidor)
				{
					RedDisponible = false;
				}
				break;
			case 3:
				RedDisponible = false;
				break;
		}
	}

	transfer[1] = sim_time;
	transfer[2] = PedidoEstacion;
	transfer[3] = nro_estacion;
	transfer[4] = 0;
	transfer[5] = false;
	transfer[6] = expon(media_servicio_estacion, FinPedido);

	if (RedDisponible)
	{
		tiempo_utilizacion = transfer[6];
		sampst(0, nro_estacion);
		list_file(LAST, Red);

		//Determinar el Fin del Pedido
		transfer[1] = sim_time + tiempo_utilizacion;
		transfer[2] = FinPedido;
		transfer[3] = PedidoEstacion;
		transfer[4] = nro_estacion;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		list_file(LAST, Pedidos);
	}
}

void OrdenarPedidos(void)
{	
	if (list_size[Pedidos] > 0)
	{
		bandera = false;
		list_remove(FIRST, Pedidos);
		while (list_size[Pedidos] >= 0 && transfer[2] != PedidoEstacion)
		{
			prioridad = transfer[3];
			switch (prioridad)
			{
			case 0:
				list_file(LAST, ColaServidor);
				break;
			case 1:
				list_file(LAST, ColaServPrioridad);
				break;
			}
			if (list_size[Pedidos] > 0)
			{
				list_remove(FIRST, Pedidos);
				if (transfer[2] == PedidoEstacion)
				{
					list_file(FIRST, Pedidos);
					return;
				}
			}
			else
			{
				return;
			}
			bandera = true;
		}
		if (bandera == false && transfer[2] == PedidoEstacion)
		{
			list_file(FIRST, Pedidos);
		}
	}
}

void JuntarPedidos(void)
{
	while (list_size[ColaServidor] > 0)
	{
		list_remove(LAST, ColaServidor);
		list_file(FIRST, Pedidos);
	}
	while (list_size[ColaServPrioridad] > 0)
	{
		list_remove(LAST, ColaServPrioridad);
		list_file(FIRST, Pedidos);
	}
}

void Rutina_PedidoServidor(void)
{
	RedDisponible = true;
	if (list_size[Red] > 0)
	{
		list_remove(FIRST, Red);
		tipo_pedido = transfer[2];
		prioridad = transfer[3];
		list_file(FIRST, list_aux);
		probabilidad = lcgrand(15);
		if (probabilidad <= 0.1)
		{
			if (tipo_pedido == PedidoServidor)
			{
				if (prioridad == 1)
				{
					// Queda el pedido que esta porque tiene prioridad
					list_remove(FIRST, list_aux);
					list_file(FIRST, Red);
					RedDisponible = false;
				}
				else
				{
					OrdenarPedidos();
					event_cancel(FinPedido);
					while (transfer[3] != PedidoServidor)
					{
						list_file(FIRST, event_aux);
						event_cancel(FinPedido);
					}
					while (list_size[event_aux] > 0)
					{
						list_remove(FIRST, event_aux);
						list_file(INCREASING, LIST_EVENT);
					}
					list_remove(FIRST, list_aux);
					transfer[4] += sim_time - transfer[1]; // Tiempo que estuvo en la red
					if (transfer[5] == false)
					{
						pedidos_desplazados++;
						transfer[5] = true;
					}
					list_file(FIRST, ColaServidor);
					transfer[1] = sim_time;
					list_file(LAST, MediaEsperaServ);

					// Si hay mas de cero es porque hay una estacion
					if (list_size[Red] > 0)
					{
						list_remove(LAST, Red);
						nro_estacion = transfer[3];
						list_file(FIRST, list_aux);
						event_cancel(FinPedido);
						while (transfer[3] != PedidoEstacion || transfer[4] != nro_estacion)
						{
							list_file(FIRST, event_aux);
							event_cancel(FinPedido);
						}
						while (list_size[event_aux] > 0)
						{
							list_remove(FIRST, event_aux);
							list_file(INCREASING, LIST_EVENT);
						}
						list_remove(FIRST, list_aux);
						transfer[4] += sim_time - transfer[1];
						if (transfer[5] == false)
						{
							pedidos_desplazados++;
							transfer[5] = true;
						}
						list_file(FIRST, Pedidos);
					}
					RedDisponible = true;
				}
			}
			else
			{
				// Solo hay estaciones y hay que sacarlas
				OrdenarPedidos();
				list_remove(FIRST, list_aux);
				list_file(FIRST, Red);
				while (list_size[Red] > 0)
				{
					list_remove(LAST, Red);
					nro_estacion = transfer[3];
					list_file(FIRST, list_aux);
					event_cancel(FinPedido);
					while (transfer[3] != PedidoEstacion || transfer[4] != nro_estacion)
					{
						list_file(FIRST, event_aux);
						event_cancel(FinPedido);
					}
					while (list_size[event_aux] > 0)
					{
						list_remove(FIRST, event_aux);
						list_file(INCREASING, LIST_EVENT);
					}
					list_remove(FIRST, list_aux);
					transfer[4] += sim_time - transfer[1];
					if (transfer[5] == false)
					{
						pedidos_desplazados++;
						transfer[5] = true;
					}
					list_file(FIRST, Pedidos);
				}
			}
		}
		// Pedido de servidor sin prioridad
		else
		{
			if (tipo_pedido == PedidoServidor)
			{

				list_remove(FIRST, list_aux);
				list_file(FIRST, Red);
				RedDisponible = false;
			}
			else
			{
				OrdenarPedidos();
				list_remove(FIRST, list_aux);
				list_file(FIRST, Red);
				while (list_size[Red] > 1)
				{
					list_remove(LAST, Red);
					nro_estacion = transfer[3];
					list_file(FIRST, list_aux);
					event_cancel(FinPedido);
					while (transfer[3] != PedidoEstacion || transfer[4] != nro_estacion)
					{
						list_file(FIRST, event_aux);
						event_cancel(FinPedido);
					}
					while (list_size[event_aux] > 0)
					{
						list_remove(FIRST, event_aux);
						list_file(INCREASING, LIST_EVENT);
					}
					list_remove(FIRST, list_aux);
					transfer[4] += sim_time - transfer[1];
					if (transfer[5] == false)
					{
						pedidos_desplazados++;
						transfer[5] = true;
					}
					list_file(FIRST, Pedidos);
				}
				RedDisponible = true;
			}
		}
	}
	if (RedDisponible)
	{
		transfer[1] = sim_time;
		transfer[2] = PedidoServidor;
		if (probabilidad > 0.1)
		{
			transfer[3] = 0;
		}
		else 
		{
			transfer[3] = 1;
		}
		transfer[4] = 0;
		transfer[5] = false;
		transfer[6] = expon(media_servicio_servidor, FinPedido);
		prioridad = transfer[3];
		tiempo_utilizacion = transfer[6];
		list_file(FIRST, Red);

		//Determinar el Fin del Pedido
		transfer[1] = sim_time + tiempo_utilizacion;
		transfer[2] = FinPedido;
		transfer[3] = PedidoServidor;
		transfer[4] = prioridad;
		list_file(INCREASING, LIST_EVENT);
	}
	else
	{
		transfer[1] = sim_time;
		transfer[2] = PedidoServidor;
		transfer[4] = 0;
		transfer[5] = false;
		transfer[6] = expon(media_servicio_servidor, FinPedido);
		if (probabilidad > 0.1)
		{
			transfer[3] = 0;
			list_file(FIRST, ColaServidor);
		}
		else
		{
			transfer[3] = 1;
			list_file(FIRST, ColaServPrioridad);
		}
		transfer[1] = sim_time;
		list_file(LAST, MediaEsperaServ);
	}

	// Juntar colas
	JuntarPedidos();

	// Determinar proximo Pedido Servidor
	transfer[1] = sim_time + expon(media_interarribos_servidor, PedidoServidor);
	transfer[2] = PedidoServidor;
	list_file(INCREASING, LIST_EVENT);
}

void Rutina_FinPedido(void)
{
	// Determinar que pedido termino
	tipo_pedido = transfer[3];
	nro_estacion = transfer[4];
	list_file(FIRST, list_aux);
	list_remove(FIRST, Red);

	if (tipo_pedido != transfer[2])
	{
		list_file(FIRST, Red);
		list_remove(LAST, Red);
	}

	if (tipo_pedido == PedidoEstacion)
	{
		// Encontrar la estacion que termino
		while (nro_estacion != transfer[3])
		{
			list_file(FIRST, Red_aux);
			list_remove(FIRST, Red);
		}
		// Volver a poner las cosas en la red
		while (list_size[Red_aux] > 0)
		{
			list_remove(FIRST, Red_aux);
			list_file(FIRST, Red);
		}
	}

	OrdenarPedidos();
	list_remove(FIRST, list_aux);
	if (tipo_pedido == PedidoEstacion)
	{
		// Generar proximo pedido de esa estacion
		transfer[1] = sim_time + expon(media_interarribos_estacion, PedidoEstacion);
		transfer[2] = PedidoEstacion;
		transfer[3] = nro_estacion;
		list_file(INCREASING, LIST_EVENT);

		// Poner otro pedido de estacion en la red
		if (list_size[Pedidos] > 0)
		{	
			list_remove(FIRST, Pedidos);
			nro_estacion = transfer[3];
			tiempo_red = transfer[4];
			tiempo_utilizacion = transfer[6];
			sampst(sim_time - transfer[1], nro_estacion);  // El nro de estacion es igual al numero de demora_Estacion
			transfer[1] = sim_time;
			list_file(LAST, Red);

			//Determinar el Fin del Pedido
			transfer[1] = sim_time + tiempo_utilizacion - tiempo_red;
			transfer[2] = FinPedido;
			transfer[3] = PedidoEstacion;
			transfer[4] = nro_estacion;
			list_file(INCREASING, LIST_EVENT);
		}
	}
	else
	{
		// Termino un servidor con prioridad y hay otro esperando
		if (transfer[4] == 1 && list_size[ColaServPrioridad] > 0)
		{
			// Se carga otro con prioridad
			list_remove(FIRST, ColaServPrioridad);
			transfer[1] = sim_time;
			prioridad = transfer[3];
			tiempo_utilizacion = transfer[6];
			list_file(FIRST, Red);
			list_remove(FIRST, MediaEsperaServ);

			//Determinar el Fin del Pedido
			transfer[1] = sim_time + tiempo_utilizacion;
			transfer[2] = FinPedido;
			transfer[3] = PedidoServidor;
			transfer[4] = prioridad;
			list_file(INCREASING, LIST_EVENT);
		}
		// Si no, se pone un pedido comun de servidor y uno de estacion
		else if (list_size[ColaServidor] > 0)
		{
			list_remove(FIRST, ColaServidor);
			transfer[1] = sim_time;
			prioridad = transfer[3];
			tiempo_red = transfer[4];
			tiempo_utilizacion = transfer[6];
			list_file(FIRST, Red);
			list_remove(FIRST, MediaEsperaServ);
			
			//Determinar el Fin del Pedido
			transfer[1] = sim_time + tiempo_utilizacion - tiempo_red;
			transfer[2] = FinPedido;
			transfer[3] = PedidoServidor;
			transfer[4] = prioridad;
			list_file(INCREASING, LIST_EVENT);

			if (list_size[Red] == 1 && list_size[Pedidos] > 0)
			{
				list_remove(FIRST, Pedidos);
				nro_estacion = transfer[3];
				tiempo_red = transfer[4];
				tiempo_utilizacion = transfer[6];
				sampst(sim_time - transfer[1], nro_estacion);
				transfer[1] = sim_time;
				list_file(LAST, Red);

				//Determinar el Fin del Pedido
				transfer[1] = sim_time + tiempo_utilizacion - tiempo_red;
				transfer[2] = FinPedido;
				transfer[3] = PedidoEstacion;
				transfer[4] = nro_estacion;
				list_file(INCREASING, LIST_EVENT);
			}
		}
		// Si no hay pedidos de servidor, se ponen estaciones
		else
		{
			while (list_size[Pedidos] > 0 && list_size[Red] < 3)
			{
				list_remove(FIRST, Pedidos);
				nro_estacion = transfer[3];
				tiempo_red = transfer[4];
				tiempo_utilizacion = transfer[6];
				sampst(sim_time - transfer[1], nro_estacion);
				transfer[1] = sim_time;
				list_file(LAST, Red);

				//Determinar el Fin del Pedido
				transfer[1] = sim_time + tiempo_utilizacion - tiempo_red;
				transfer[2] = FinPedido;
				transfer[3] = PedidoEstacion;
				transfer[4] = nro_estacion;
				list_file(INCREASING, LIST_EVENT);
			}
		}
	}
	JuntarPedidos();
}

void Rutina_Falla(void)
{
	falla++;

	while (list_size[Red] > 0)
		list_remove(FIRST, Red);

	while (list_size[Pedidos] > 0)
		list_remove(FIRST, Pedidos);

	while (list_size[LIST_EVENT] > 0)
		list_remove(FIRST, LIST_EVENT);

	while (list_size[MediaEsperaServ] > 0)
		list_remove(FIRST, MediaEsperaServ);

	// Reiniciar sistema
	// Cargar la lista de eventos con los eventos que inicializan la simulacion
	for (int i = 0; i < 6; i++)
	{
		transfer[1] = sim_time + expon(media_interarribos_estacion, PedidoEstacion);
		transfer[2] = PedidoEstacion;
		transfer[3] = i + 1;
		list_file(INCREASING, LIST_EVENT);
	}

	transfer[1] = sim_time + expon(media_interarribos_servidor, PedidoServidor);
	transfer[2] = PedidoServidor;
	list_file(INCREASING, LIST_EVENT);

	transfer[1] = sim_time + uniform(media_falla_min, media_falla_max, Falla);
	transfer[2] = Falla;
	list_file(INCREASING, LIST_EVENT);
}

void Reporte(void)
{
	printf("ESTADISTICAS\n");

	printf("\nCantidad de Pedidos de Estacion: %i\n", cant_estacion);
	printf("Cantidad de Pedidos de Servidor: %i\n", cant_servidor);

	filest(Red);
	printf("\nUtilizacion de la Red: %.2f por ciento \n ", transfer[1]/3*100);

	sampst(0, -Demora_estacion1);
	printf("\nDemora Media de espera de los pedidos de la estacion 1: %.3f \n ", transfer[1]);
	sampst(0, -Demora_estacion2);
	printf("\nDemora Media de espera de los pedidos de la estacion 2: %.3f \n ", transfer[1]);
	sampst(0, -Demora_estacion3);
	printf("\nDemora Media de espera de los pedidos de la estacion 3: %.3f \n ", transfer[1]);
	sampst(0, -Demora_estacion4);
	printf("\nDemora Media de espera de los pedidos de la estacion 4: %.3f \n ", transfer[1]);
	sampst(0, -Demora_estacion5);
	printf("\nDemora Media de espera de los pedidos de la estacion 5: %.3f \n ", transfer[1]);
	sampst(0, -Demora_estacion6);
	printf("\nDemora Media de espera de los pedidos de la estacion 6: %.3f \n ", transfer[1]);

	printf("\nCantidad de pedidos que fueron desplazados por un pedido de Servidor: %i \n ", pedidos_desplazados);

	filest(Pedidos);
	printf("\nCantidad Media de pedidos en espera: %.3f \n ", transfer[1]);
	
	filest(MediaEsperaServ);
	printf("\nCantidad Media de pedidos de servidor en espera: %.3f \n", transfer[1]);

	printf("\nCantidad de fallas ocurridas: %i \n", falla);
}