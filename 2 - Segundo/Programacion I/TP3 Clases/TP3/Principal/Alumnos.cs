using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Alumno : Persona
    {
        private string carrera;
        public string Carrera
        {
            get { return carrera; }
            set { carrera = value; }
        }

        private List<int> nota;
        public List<int> Nota
        {
            get { return nota; }
            set { nota = value; }
        }
        public Alumno()
        {
            nota = new List<int>();
        }

        public void AgregarNotas(int n)
        {
            nota.Add(n);
        }

        private int suma;
        public float ObtenerPromedio()
        {
            suma = 0;
            foreach (int i in nota)
            {
                suma = suma + i;
            }
            return (suma / nota.Count());
        }

        private string datos;
        public override string MostrarDatos()
        {
            datos = Nombre + " - Notas:";
            foreach (int i in nota)
            {
                datos = datos + " " + i;
            }
            return datos;
        }
    }
}
