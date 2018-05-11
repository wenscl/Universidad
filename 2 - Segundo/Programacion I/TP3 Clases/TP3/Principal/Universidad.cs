using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    public class Universidad
    {
        private string nombre;
        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        private string sede;
        public string Sede
        {
            get { return sede; }
            set { sede = value; }
        }

        private int telefono;
        public int Telefono
        {
            get { return telefono; }
            set { telefono = value; }
        }

        private string direccion;
        public string Direccion
        {
            get { return direccion; }
            set { direccion = value; }
        }

        private List<Carrera> carrera;
        public List<Carrera> Carrera
        {
            get { return carrera; }
            set { carrera = value; }
        }
        
        public Universidad()
        {
            carrera = new List<Carrera>();
            mejorespromedios = new List<Alumno>();
            personal = new List<Personal>();
        }

        public Universidad(string nom)
        {
            carrera = new List<Carrera>();
            nombre = nom;
        }
        
        public void AgregarCarrera(Carrera c)
        {
            Carrera.Add(c);
        }

        private List<Personal> personal;
        public List<Personal> Personal
        {
            get { return personal; }
            set { personal = value; }
        }

        public void AgregarPersonal(Personal p)
        {
            Personal.Add(p);
        }

        private List<Alumno> mejorespromedios;
        public List<Alumno> MejoresPromedios
        {
            get { return mejorespromedios; }
            set { mejorespromedios = value; }
        }
        
        private int edad;
        private DateTime fecha;
        private int jovenes;
        public int ProfesoresYPromedios()
        {
            jovenes = 0;
            foreach (Carrera i in carrera)
            {
                foreach (Curso p in i.Curso)
                {
                    foreach (Materia j in p.Materia)
                    {
                        foreach (Profesor l in j.Profesor)
                        {
                            fecha = DateTime.Now;
                            edad = fecha.Year - l.Fechanacimiento.Year;
                            if ((fecha.Month < l.Fechanacimiento.Month) || (fecha.Month == l.Fechanacimiento.Month && fecha.Day < l.Fechanacimiento.Day))
                            {
                                edad = edad - 1;
                            }
                            if (edad < 35)
                            {
                                jovenes = jovenes + 1;
                            }
                        }
                        if (((p.Año == "Informatica 2013") && (j.Año == "Segundo año")) || (j.Nombre == "Programacion I"))
                        {
                            foreach (Alumno v in j.Alumno)
                            {
                                if (v.ObtenerPromedio() > 8)
                                {
                                    mejorespromedios.Add(v);
                                }
                            }
                        }
                    }
                }
            }
            return jovenes;
        }
        
    }
}
