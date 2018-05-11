using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public class Carta
    {
        public Carta(string nombre, string codigo)
        {
            if (string.IsNullOrEmpty(codigo) || string.IsNullOrEmpty(nombre))
            { throw new ArgumentNullException("Debe establecer el nombre y el código de la carta"); }

            this.Codigo = codigo;
            this.Nombre = nombre;
            this.Atributos = new List<Atributo>();
        }

        public string Codigo { get; set; }
        public string Nombre { get; set; }
        public IList<Atributo> Atributos { get; set; }

        public void AgregarAtributo(TipoAtributo nombre, double valor)
        {
            var atributo = new Atributo(nombre, valor);

            if (Atributos.Where(x => x.Nombre == atributo.Nombre).Count() != 0)
            { throw new ArgumentException("Los atributos no pueden repetirse"); }

            Atributos.Add(atributo);
        }
        
        public void CantidadAtributosTest()
        {
            if (Atributos.Count() == 0)
            { throw new ArgumentNullException("Debe establecer como mínimo 1 atributo"); }
        }
    }
}