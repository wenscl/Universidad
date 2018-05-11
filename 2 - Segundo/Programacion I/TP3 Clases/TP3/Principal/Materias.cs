using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Materia
    {
        private string nombre;
        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        private string planificacion;
        public string Planificacion
        {
            get { return planificacion; }
            set { planificacion = value; }
        }

        private string año;
        public string Año
        {
            get { return año; }
            set { año = value; }
        }

        private List<Alumno> alumno;
        public List<Alumno> Alumno
        {
            get { return alumno; }
            set { alumno = value; }
        }

        public void AgregarAlumno(Alumno a)
        {
            Alumno.Add(a);
        }
        private List<Profesor> profesor;
        public List<Profesor> Profesor
        {
            get { return profesor; }
            set { profesor = value; }
        }

        public Materia()
        {
            profesor = new List<Profesor>();
            alumno = new List<Alumno>();
        }

        public void AgregarProfesor(Profesor p)
        {
            Profesor.Add(p);
        }
    }
}
