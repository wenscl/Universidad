using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using JuegoCromy.Code;

namespace JuegoCromy.Test
{
    [TestClass]
    public class JugadorTest
    {
        [TestMethod]
        public void PuedoCrearJugadorConNombre()
        {
            var jugador1 = new Jugador("Wen");
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoCrearJugadorSinNombre()
        {
            var jugador1 = new Jugador("");
        }

        [TestMethod]
        public void PerderMano()
        {
            var jugador1 = new Jugador("Wendy");
            var jugador2 = new Jugador("Gio");
            var mazo = new Mazo("Cartoon Network", 30);
            for (int x = 0; x < 30; x++)
            {
                string y = x.ToString();
                var carta = new Carta("Tom", "CN" + y);
                mazo.AgregarCarta(carta);
            }
            mazo.Mezclar();
            var partida = new Partida("CN", jugador1, "Cartoon Network");
            partida.AgregarJugadores(jugador2);
            partida.Repartir();
            jugador1.PerderCarta();
        }

        [TestMethod]
        public void GanarMano()
        {
            var jugador1 = new Jugador("Wendy");
            var jugador2 = new Jugador("Gio");
            var mazo = new Mazo("Cartoon Network", 30);
            for (int x = 0; x < 30; x++)
            {
                string y = x.ToString();
                var carta = new Carta("Tom", "CN" + y);
                mazo.AgregarCarta(carta);
            }
            mazo.Mezclar();
            var partida = new Partida("CN", jugador1, "Cartoon Network");
            partida.AgregarJugadores(jugador2);
            partida.Repartir();
            jugador1.GanarCarta(jugador2.Cartas[0]);
        }
    }
}
