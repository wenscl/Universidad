using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using JuegoCromy.Code;

namespace JuegoCromy.Test
{
    [TestClass]
    public class PartidaTest
    {
        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoCrearPartidaSinNombre()
        {
            var jugador = new Jugador("Wendy");
            var partida = new Partida(null, jugador, "Cartoon Network");
        }

        [TestMethod]
        public void PuedoCrearPartidaConNombre()
        {
            var jugador = new Jugador("Wendy");
            var partida = new Partida("PartidaCN", jugador, "Cartoon Network");
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoCrearPartidaSinJugador()
        {
            var partida = new Partida("PartidaCN", null, "Cartoon Network");
        }
    }
}
