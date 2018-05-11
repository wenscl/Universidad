using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Personal : Persona
    {
        private string ocupacion;
        public string Ocupacion
        {
            get { return ocupacion; }
            set { ocupacion = value; }
        }

        private string titulo;
        public string Titulo
        {
            get { return titulo; }
            set { titulo = value; }
        }
    }
}
