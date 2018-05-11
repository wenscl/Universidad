using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Alumno alumno1 = new Alumno();
            alumno1.Nombre = "Seba";
            alumno1.Sexo = "xxxxxxx";
            alumno1.MostrarNombreySexo();


            Alumno alumno2 = new Alumno();
            alumno2.Nombre = "Juan";

            Alumno alumno3 = new Alumno("Fede");

            Alumno alumno4 = new Alumno("Pepito", "Masculino");

            //var alumno5 = new Alumno()
            //{
            //    Nombre = "Cachito",
            //    Sexo = "Femenino"
            //};

            Console.WriteLine(alumno1.Nombre);
            Console.WriteLine(alumno1.Sexo);
            
            Profesor profesor1 = new Profesor();
            profesor1.MostrarNombreySexo();

            Curso cursoProgramacionUno = new Curso();
            cursoProgramacionUno.Profesor = profesor1;
          
            cursoProgramacionUno.AgregarAlumno(alumno1);
            cursoProgramacionUno.AgregarAlumno(alumno2);
            //...

            Persona persona1 = (Persona) profesor1;

            //Console.Write(profesor1.ObtenerProfesion());

            List<Persona> personas = new List<Persona>();
            personas.Add(alumno1);
            personas.Add(profesor1);

            foreach (var p in personas)
            {
                p.Metodo();
            }

            //Persona persona1 = new Persona();

            //alumno1.CambiarNombre("Pepito");
            //Console.Write(alumno1.ObtenerNombreEnMayuscula());

            //Es un comentario.
            Console.Read();
        }
    }
}
