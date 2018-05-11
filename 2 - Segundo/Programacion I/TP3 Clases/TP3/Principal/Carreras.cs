using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Carrera
    {
        private string nombre;
        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        private string duracion;
        public string Duracion
        {
            get { return duracion; }
            set { duracion = value; }
        }

        private string plan;
        public string Plan
        {
            get { return plan; }
            set { plan = value; }
        }

        private string coordinador;
        public string Coordinador
        {
            get { return coordinador; }
            set { coordinador = value; }
        }

        private List<Curso> curso;
        public List<Curso> Curso
        {
            get { return curso; }
            set { curso = value; }
        }
        public Carrera()
        {
            curso= new List<Curso>();
        }

        public void AgregarCurso(Curso c)
        {
            Curso.Add(c);
        }

    }
}
