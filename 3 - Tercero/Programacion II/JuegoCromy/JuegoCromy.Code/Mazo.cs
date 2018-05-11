using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public class Mazo
    {
        public Mazo( string nombre, int cantidaddecartas)
        {
            if (string.IsNullOrEmpty(nombre) || cantidaddecartas <= 0)
            { throw new ArgumentNullException("Nombre vacío o cantidad de cartas incorrecta."); }

            this.Nombre = nombre;
            this.CantidadDeCartas = cantidaddecartas;
            this.Cartas = new List<Carta>();
            this.Atributos = new List<TipoAtributo>();
            this.NombreAtributos = new List<string>();
        }
        
        public string Nombre { get; set; }
        public int CantidadDeCartas { get; set; }
        public IList<Carta> Cartas { get; set; }
        public IList<TipoAtributo> Atributos { get; set; }
        public List<string> NombreAtributos { get; set; }

        public void AgregarCarta(Carta NuevaCarta)
        {
            if (Cartas.Where(x => x.Codigo == NuevaCarta.Codigo).Count() != 0)
            { throw new ArgumentException("La carta ya existe."); }

            if (Cartas.Count() > CantidadDeCartas)
            { throw new ArgumentException("Máximo de cartas especificadas alcanzado."); }

            Cartas.Add(NuevaCarta);
        }

        public void Mezclar() 
        {
            Cartas.Mezclar();
        }

        public void ControlCantidadCartas()
        {
            if ((Cartas.Count() == 0) || (Cartas.Count() < CantidadDeCartas))
                throw new ArgumentException("Cantidad de cartas incorrecta.");
        }
    }
}
