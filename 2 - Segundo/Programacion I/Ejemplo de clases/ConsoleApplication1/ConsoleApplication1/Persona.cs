using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public class Persona
    {
        private string nombre;

        public string Nombre
        {
            get
            {
                return nombre;
            }

            set
            {
                nombre = value;
            }
        }

        private string sexo;

        public string Sexo
        {
            get { return sexo; }

            set
            {
                if (value != "Masculino" && value != "Femenino")
                {
                    sexo = "Indefinido";
                }
                else
                {
                    sexo = value;
                }
            }
        }

        public virtual string Metodo()
        {
            return "";
        }

        public string MostrarNombreySexo()
        {
            return nombre + ' ' + sexo;
        }
    }
}
