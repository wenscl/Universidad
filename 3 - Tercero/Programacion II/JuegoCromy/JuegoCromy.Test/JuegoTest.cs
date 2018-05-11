using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using JuegoCromy.Code;

namespace JuegoCromy.Test
{
    [TestClass]
    public class JuegoTest
    {
        [TestMethod]
        public void PuedoCrearJuegoConPartidas()
        {
            var juego = new Juego();
            var jugador1 = new Jugador("Wendy");
            var partida = new Partida("PartidaCN", jugador1, "Cartoon Network");
            juego.AgregarPartida(partida);
        }
    }
}
