%%%%%%%%%%%%%%%%%% HECHOS como se dio en clase %%%%%%%%%%%%%%%%%%
torneo_jugadores('Torneo de los caballos','Romina Alemandi').
torneo_jugadores('Torneo de los caballos','Ruben Dario').
torneo_jugadores('Torneo nacional de las torres blancas','Romina Alemandi').
torneo_jugadores('Torneo nacional de las torres blancas','Ruben Dario').

%%%%%%%%%%%%%%%%%% REGLAS para los hechos de arriba %%%%%%%%%%%%%%%%%%
participantes(Torneo,Jugador):-torneo_jugadores(Torneo,Jugador).

%%%%%%%%%%%%%%%%%% Crear hechos accediendo a la base de datos %%%%%%%%%%%%%%%%%%
%CONEXION. Antes de trabajar con ejecuciones, se abre la conexion.
abrir_conexion:- odbc_connect('swiprolog', _,
                 [ user(postgres),
                 password(postgres),
                 alias(swiprolog),
                 open(once) ]).
cerrar_conexion:- odbc_disconnect('swiprolog').

%%%%%%%%%%%%%%%%%% HECHOS %%%%%%%%%%%%%%%%%%
%Ejemplo de como insertar torneos en la BD
insertar_torneo(F):- odbc_query('swiprolog',
                    'INSERT INTO "torneo"("nombre","fecha_inicio","fecha_fin") VALUES(''torneo_nacional_de_las_torres_blancas'',''2016-06-23'',''2016-07-23'')',
                    affected(F)).

%Consultar los datos en la base de datos
torneo(Nombre,Fecha_i, Fecha_f):- odbc_query('swiprolog',
                                  'SELECT "nombre", CAST("fecha_inicio" AS character varying(60)), CAST("fecha_fin" AS character varying(60)) FROM "torneo"',
                                  row(Nombre,Fecha_i,Fecha_f)).

jugadores_torneo(Torneo,Jugador):- odbc_query('swiprolog',
                                  'SELECT "torneo", "jugador" FROM "torneo_jugadores"',
                                  row(Torneo,Jugador)).

jugadores_partidas(Torneo,Jugador1,Jugador2):- odbc_query('swiprolog',
                                  'SELECT "torneo", "jugador_blanco","jugador_negro" FROM "partida"',
                                  row(Torneo,Jugador1,Jugador2)).
                                  
ganador(Torneo,Jugador1,Jugador2,Ganador):- odbc_query('swiprolog',
                                  'SELECT "torneo", "jugador_blanco","jugador_negro","jugador_ganador" FROM "partida"',
                                  row(Torneo,Jugador1,Jugador2,Ganador)).

torneo_club(Torneo,Club):- odbc_query('swiprolog',
                                  'SELECT "nombre_torneo", "nombre_club" FROM "torneo_clubes"',
                                  row(Torneo,Club)).
                                  
jugadas(Jugador,Jugada):- odbc_query('swiprolog',
                                  'SELECT "jugador", "movimiento" FROM "jugada"',
                                  row(Jugador,Jugada)).

%%%%%%%%%%%%%%%%%% REGLAS %%%%%%%%%%%%%%%%%%
consultar_torneo(Torneo,Fecha_i,Fecha_f):- torneo(Torneo,Fecha_i, Fecha_f).

consultar_participantes_torneo(Torneo,Jugador):- jugadores_torneo(Torneo,Jugador).

consultar_contrincantes_color(Torneo,Jugador_blanco,Jugador_negro):-jugadores_partidas(Torneo,Jugador_blanco,Jugador_negro).

consultar_contrincantes(Torneo,Jugador_blanco,Jugador_negro):-jugadores_partidas(Torneo,Jugador_blanco,Jugador_negro);jugadores_partidas(Torneo,Jugador_negro,Jugador_blanco).

consultar_ganador(Torneo,Jugador1,Jugador2,Ganador):-ganador(Torneo,Jugador1,Jugador2,Ganador);ganador(Torneo,Jugador2,Jugador1,Ganador).

consultar_clubes(Torneo,Club):-torneo_club(Torneo,Club).

consultar_jugadas(Jugador,Jugada):-jugadas(Jugador,Jugada).