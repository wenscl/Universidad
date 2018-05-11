using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{

    public class Alumno : Persona
    {
        public Alumno()
        {
            Nombre = "S/N";
        }

        public Alumno(string nombre)
        {
            Nombre = nombre;
        }

        public Alumno(string nombre, string sexo)
        {
            Nombre = nombre;
            Sexo = sexo;
        }

        public override string Metodo()
        {
            return "A";
        }
    }
}
