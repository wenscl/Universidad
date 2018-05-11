using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using JuegoCromy.Code;

namespace JuegoCromy.Test
{
    [TestClass]
    public class MazoTest
    {
        [TestMethod]
        public void PuedoAgregarUnaCarta()
        {
            var carta = new Carta("Las chicas superpoderosas", "CN1");
            carta.AgregarAtributo(TipoAtributo.Fuerza, 20);
            var mazo = new Mazo("Cartoon Network", 1);
            mazo.AgregarCarta(carta);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoUsarUnMazoVacio()
        {
            var mazo1 = new Mazo("Cartoon Network", 0);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void NoPuedoUsarCantidadIncorrectaDeCartas()
        {
            var mazo1 = new Mazo("Cartoon Network", 10);
            var carta = new Carta("Las chicas superpoderosas", "CN1");
            carta.AgregarAtributo(TipoAtributo.Fuerza, 20);
            mazo1.ControlCantidadCartas();
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void NoPuedoAgregarCartasIguales()
        {
            var carta1 = new Carta("Las chicas superpoderosas", "CN1");
            carta1.AgregarAtributo(TipoAtributo.Fuerza, 20);
            var carta2 = new Carta("Las chicas superpoderosas", "CN1");
            carta2.AgregarAtributo(TipoAtributo.Peso, 53);
            var mazo = new Mazo("Cartoon Network", 32);
            mazo.AgregarCarta(carta1);
            mazo.AgregarCarta(carta2);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void NoPuedoCrearUnMazoConMasCartasDeLasEspecificadas()
        {
            var mazo = new Mazo("Cartoon Network", 32);
            for (int x = 0; x < 60; x++)
            {
                string y = x.ToString();
                var carta = new Carta("Las chicas superpoderosas", "CN" + y);
                mazo.AgregarCarta(carta);
            }
        }
    }
}