using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using JuegoCromy.Code;

namespace JuegoCromy.Test
{
    [TestClass]
    public class CartasTest
    {   
        [TestMethod]
        public void PuedoCrearUnaCartaConCodigoYNombre()
        {
            var carta = new Carta("Las chicas superpoderosas", "CN1");
            carta.AgregarAtributo(TipoAtributo.Fuerza, 90);
            Assert.IsNotNull(carta.Codigo);
            Assert.IsNotNull(carta.Nombre);
        }

        [TestMethod]
        public void PuedoCrearUnaCartaConAtributos()
        {
            var carta = new Carta("Las chicas superpoderosas", "CN1");
            carta.AgregarAtributo(TipoAtributo.Maldad, 10);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoCrearUnaCartaSinCodigoYNombre()
        {
            var carta = new Carta (null, null);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoCrearUnaCartaConCodigoYNombreVacio()
        {
            var carta = new Carta("","");
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentNullException))]
        public void NoPuedoCrearUnaCartaSinAtributos()
        {
            var carta = new Carta("Las chicas superpoderosas", "CN1");
            carta.CantidadAtributosTest();
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void NoPuedoAgregarCartasConAtributosRepetidos()
        {
            var carta = new Carta("Las chicas superpoderosas", "CN1");
            carta.AgregarAtributo(TipoAtributo.Valentia, 90);
            carta.AgregarAtributo(TipoAtributo.Valentia, 90);     
        }
    }
}
