using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Principal
{
    class Program
    {
        static void Main(string[] args)
        {
            Universidad universidad = new Universidad();
            universidad.Nombre = "Universidad Catolica de Santiago del Estero";

            Carrera carrera1 = new Carrera();
            universidad.AgregarCarrera(carrera1);
            carrera1.Nombre = "Ingenieria en Informatica";

            Curso curso1 = new Curso();
            carrera1.AgregarCurso(curso1);
            curso1.Año = "Informatica 2014";

            Materia materia1 = new Materia();
            curso1.AgregarMateria(materia1);
            materia1.Nombre = "Introduccion a la Programacion";
            materia1.Año = "Primer año";

            Profesor profesor1 = new Profesor();
            materia1.AgregarProfesor(profesor1);
            profesor1.Nombre = "Ernesto Perez";
            profesor1.Sexo = "Masculino";
            profesor1.Titulo = "Ingeniero, Profesor asitente";
            profesor1.Fechanacimiento = DateTime.Parse("30/04/1987");

            Alumno alumno1 = new Alumno();
            materia1.AgregarAlumno(alumno1);
            alumno1.Nombre = "Juan Hernandez";
            alumno1.Sexo = "Masculino";
            alumno1.DNI = 38592444;
            alumno1.Domicilio = "Falucho 265";
            alumno1.Fechanacimiento = DateTime.Parse("20/10/1995");
            alumno1.Carrera = carrera1.Nombre;
            alumno1.AgregarNotas(10);
            alumno1.AgregarNotas(8);

            Alumno alumno2 = new Alumno();
            materia1.AgregarAlumno(alumno2);
            alumno2.Nombre = "Elsa Fernandez";
            alumno2.Sexo = "Femenino";
            alumno2.AgregarNotas(6);

            Curso curso2 = new Curso();
            carrera1.AgregarCurso(curso2);
            curso2.Año = "Informatica 2013";
            
            Materia materia2 = new Materia();
            curso2.AgregarMateria(materia2);
            materia2.Nombre = "Programacion I";
            materia2.Año = "Segundo año";

            Profesor profesor2 = new Profesor();
            materia2.AgregarProfesor(profesor2);
            profesor2.Nombre = "Pedro Garcia";
            profesor2.Sexo = "Masculino";
            profesor2.Titulo = "Ingeniero, profesor asistente";

            Alumno alumno3 = new Alumno();
            materia2.AgregarAlumno(alumno3);
            alumno3.Nombre = "Maria Lopez";
            alumno3.Sexo = "Femenino";
            alumno3.AgregarNotas(9);
            alumno3.AgregarNotas(10);

            Alumno alumno4 = new Alumno();
            materia2.AgregarAlumno(alumno4);
            alumno4.Nombre = "Lucas Alvarez";
            alumno4.Sexo = "Masculino";
            alumno4.AgregarNotas(4);
            alumno4.AgregarNotas(10);

            Carrera carrera2 = new Carrera();
            universidad.AgregarCarrera(carrera2);
            carrera2.Nombre = "Licenciatura en Psicologia";

            Personal personal1 = new Personal();
            universidad.AgregarPersonal(personal1);
            personal1.Nombre = "Ana Gonzalez";
            personal1.Sexo = "Femenino";
            personal1.Ocupacion = "Secretaria docente";

            Personal personal2 = new Personal();
            universidad.AgregarPersonal(personal2);
            personal2.Nombre = "Julio Herrera";
            personal2.Sexo = "Masculino";
            personal2.Ocupacion = "Decano, profesor Titular";
            personal2.Titulo = "Doctor";

            Personal personal3 = new Personal();
            universidad.AgregarPersonal(personal3);
            personal3.Nombre = "Jorge Gomez";
            personal3.Sexo = "Masculino";
            personal3.Ocupacion = "Rector, profesor Titular";
            personal3.Titulo = "Doctor";

            Console.WriteLine(universidad.Nombre);
            Console.WriteLine("");
            foreach (Carrera i in universidad.Carrera)
            {
                Console.WriteLine(i.Nombre);
                Console.WriteLine("");
                foreach (Curso j in i.Curso)
                {
                    Console.WriteLine(j.Año);
                    Console.WriteLine("");
                    foreach (Materia k in j.Materia)
                    {
                        Console.WriteLine(k.Nombre);
                        foreach (Profesor l in k.Profesor)
                        {
                            Console.WriteLine(l.MostrarDatos());
                        }
                        Console.WriteLine("");
                        foreach (Alumno m in k.Alumno)
                        {
                            Console.WriteLine(m.MostrarDatos());
                        }
                        Console.WriteLine("");
                    }
                }
            }
            Console.WriteLine("");
            foreach (Personal f in universidad.Personal)
            {
                Console.WriteLine(f.Nombre + " - " + f.Ocupacion);
            }
            Console.WriteLine("");
            Console.WriteLine("Cantidad de profesores menores a 35 años: " + universidad.ProfesoresYPromedios());
            Console.WriteLine("");
            foreach (Alumno s in universidad.MejoresPromedios)
            {
                Console.WriteLine(s.Nombre);
            }
            Console.Read();
        }
    }
}
