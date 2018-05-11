using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Cumpleanios
{
    public class Persona
    {
        private string nombre;
        private string apellido;
        private int edad;

        public string Nombre
        {
            get { return this.nombre; }
        }
        public string Apellido
        {
            get { return this.apellido; }
        }
        public int Edad
        {
            get { return this.edad; }
        }

        public Persona(string nombred, string apellidod, int edadd)
	    {
		    this.nombre = nombred;
		    this.apellido = apellidod;
            if (edadd >= 0)
                this.edad = edadd;
            else 
                this.edad = 0;
	    }
        public event EventHandler<CumplirAniosEventArgs> CumplioAnios;
        public void Cumplir_Anios()
        {
            this.edad++;
            if (CumplioAnios != null)
                CumplioAnios(this, new CumplirAniosEventArgs(nombre, edad));
        }
        public override string ToString()
	    {
            return this.nombre + " " + this.apellido;
	    }
        public virtual void Trabajar() {}
        public void MostrarEdad()
        {
            Console.WriteLine("La edad de la persona es {0} años.", this.edad);
        }
    }
}
