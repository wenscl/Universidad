namespace JuegoCromix.Web.Hubs
{
    using JuegoCromy.Code;
    using Microsoft.AspNet.SignalR;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Web;
    public class JuegoHub : Hub
    {
        private static Juego juego = new Juego();
        public void CrearPartida(string usuario, string partida, string mazo)
        {
            // TODO: lógica para agregar la partida al juego.
            var jugador1 = new Jugador(usuario);
            jugador1.ConnectionId = this.Context.ConnectionId;

            var partida1 = new Partida(partida, jugador1, mazo);

            // Notifico a los otros usuarios de la nueva partida.

            Clients.Others.AgregarPartida(partida1);
            this.Groups.Add(this.Context.ConnectionId, partida);
            Clients.Caller.esperarJugador();

            partida1.ArmarMazo(mazo);

            juego.AgregarPartida(partida1);
        }

        public void UnirsePartida(string usuario, string partida)
        {
            var partida1 = juego.Partidas.Where(x => x.Nombre == partida).Single();
            
            // TODO: lógica para unirse a la partida al juego.
            var jugador2 = new Jugador(usuario);
            jugador2.ConnectionId = this.Context.ConnectionId;
            
            partida1.AgregarJugadores(jugador2);

            // Notifico a los otros usuarios de la nueva partida.
            Clients.All.eliminarPartida(partida);
            this.Groups.Add(this.Context.ConnectionId, partida);
            Clients.Caller.esperarPartida();
            
            // TODO: Lógica para mezclar.
            partida1.MazoCartas.Mezclar();
            partida1.Repartir();

            Clients.Group(partida).dibujarTablero(partida1.Jugadores[0], partida1.Jugadores[1], partida1.MazoCartas);
        }

        public void ObtenerPartidas()
        {
            var partidas = juego.Partidas.Where(x => x.Jugadores.Count() == 1).ToList();

            // TODO: lógica para obtener las partidas que actualmente están en espera de un jugador.
            Clients.Caller.agregarPartidas(partidas);
        }
        public void Cantar(string atributo, string codigoCarta)
        {
            var partida1 = juego.Partidas.Where(x => x.Jugadores.Where(y => y.ConnectionId == this.Context.ConnectionId).Any()).Single();
            var jugador1 = partida1.Jugadores.Where(y => y.ConnectionId == this.Context.ConnectionId).Single();
            var jugador2 = partida1.Jugadores.Where(y => y.ConnectionId != this.Context.ConnectionId).Single();
            var carta1 = jugador1.Cartas.First();
            var carta2 = jugador2.Cartas.First();
            var atributo1 = carta1.Atributos.Where(p => p.Nombre.ToString() == atributo).Single();
            var atributo2 = carta2.Atributos.Where(p => p.Nombre.ToString() == atributo).Single();
            if (atributo1.Valor >= atributo2.Valor)
            {
                jugador1.GanarCarta(carta2);
                jugador2.PerderCarta();
                Clients.Client(jugador1.ConnectionId).ganarMano();
                Clients.Client(jugador2.ConnectionId).perderMano();
            }
            else
            {
                jugador2.GanarCarta(carta1);
                jugador1.PerderCarta();
                Clients.Client(jugador2.ConnectionId).ganarMano();
                Clients.Client(jugador1.ConnectionId).perderMano();
            }

            if (jugador1.Cartas.Count == 0)
            {
                Clients.Client(jugador2.ConnectionId).ganar();
                Clients.Client(jugador1.ConnectionId).perder();
            }
            else if (jugador2.Cartas.Count == 0)
            {
                Clients.Client(jugador1.ConnectionId).ganar();
                Clients.Client(jugador2.ConnectionId).perder();
            }
        }

        public void ObtenerMazos()
        {
            var mazos = new List<string>() { "Cartoon Network", "Cyber Heroes III", "Dragon Ball Z", "Dream Team", "Marvel", "Personajes Historicos", "Procesadores", "Super Héroes" };

            // TODO: lógica para obtener los mazos de cartas.

            Clients.Caller.agregarMazos(mazos);
        }
    }
}