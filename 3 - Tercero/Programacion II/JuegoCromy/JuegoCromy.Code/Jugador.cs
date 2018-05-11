using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public class Jugador
    {
        public Jugador(string nombre)
        {
            if (string.IsNullOrEmpty(nombre))
            { throw new ArgumentNullException("Debe establecer su nombre."); }

            this.Nombre = nombre;
            this.Cartas = new List<Carta>();
        }

        public string Nombre { get; set; }
        public string ConnectionId { get; set; }
        public IList<Carta> Cartas { get; set; }

        public Carta PerderCarta()
        {
            var CartaPropia = this.Cartas.First();
            this.Cartas.Remove(CartaPropia);

            if (Cartas.Where(x => x.Codigo == CartaPropia.Codigo).Count() != 0)
            { throw new ArgumentException("La carta no fue removida."); }

            return CartaPropia;
        }

        public void GanarCarta(Carta CartaOponente)
        {
            var CartaPropia = this.Cartas.First();
            this.Cartas.Remove(CartaPropia);
            this.Cartas.Add(CartaPropia);
            this.Cartas.Add(CartaOponente);

            if (this.Cartas.Last() != CartaOponente)
            { throw new ArgumentException("La carta no se pasó al final"); }
        }
    }
}
