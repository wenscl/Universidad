using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public abstract class Persona
    {
        private string nombre;
        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        private DateTime fechanacimiento;
        public DateTime Fechanacimiento
        {
            get { return fechanacimiento; }
            set { fechanacimiento = value; }
        }

        private int dni;
        public int DNI
        {
            get { return dni; }
            set { dni = value; }
        }

        private string nacionalidad;
        public string Nacionalidad
        {
            get { return nacionalidad; }
            set { nacionalidad = value; }
        }

        private string domicilio;
        public string Domicilio
        {
            get { return domicilio; }
            set { domicilio = value; }
        }

        private string sexo;
        public string Sexo
        {
            get { return sexo; }
            set { sexo = value; }
        }

        private int altura;
        public int Altura
        {
            get { return altura; }
            set { altura = value; }
        }
        public virtual string MostrarDatos()
        {
            return "";
        }
    }
}
