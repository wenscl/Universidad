
%CONEXION
abrir_conexion:- odbc_connect('swiprolog', _,
                 [ user(postgres),
                 password(postgres),
                 alias(swiprolog),
                 open(once) ]).

%HECHO
jugadores_torneo(Torneo,Jugador):- odbc_query('swiprolog',
                                  'SELECT "torneo", "jugador" FROM "torneo_jugadores"',
                                  row(Torneo,Jugador)).

%REGLA
consultar_participantes_torneo(Torneo,Jugador):- jugadores_torneo(Torneo,Jugador).