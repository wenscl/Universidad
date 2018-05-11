using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Curso
    {
        private string año;
        public string Año
        {
            get { return año; }
            set { año = value; }
        }

        private List<Materia> materia;
        public List<Materia> Materia
        {
            get { return materia; }
            set { materia = value; }
        }
        public Curso()
        {
            materia = new List<Materia>();
        }

        public void AgregarMateria(Materia m)
        {
            Materia.Add(m);
        }
    }
}
