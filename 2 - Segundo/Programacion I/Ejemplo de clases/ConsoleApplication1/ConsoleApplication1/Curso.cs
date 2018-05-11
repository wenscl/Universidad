using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public class Curso
    {
        public Curso()
        {
            Alumnos = new List<Alumno>();
        }

        public string Materia { get; set; }
        public Profesor Profesor { get; set; }
        public List<Alumno> Alumnos { get; set; }

        public void AgregarAlumno(Alumno a)
        {
            Alumnos.Add(a);
        }

        public int CantidadAlumnos()
        {
            return Alumnos.Count();
        }
    }
}
