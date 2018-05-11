using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public class Atributo
    {
        public Atributo(TipoAtributo nombre, double valor)
        {
            this.Valor = valor;
            this.Nombre = nombre;
        }

        public TipoAtributo Nombre { get; set; }
        public double Valor { get; set; }
    }
}
