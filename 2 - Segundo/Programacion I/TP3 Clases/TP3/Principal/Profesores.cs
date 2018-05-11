using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Profesor : Persona
    {
        private string titulo;
        public string Titulo
        {
            get { return titulo; }
            set { titulo = value; }
        }

        public override string MostrarDatos()
        {
            return (Nombre + " - " + Titulo);
        }
    }
}
