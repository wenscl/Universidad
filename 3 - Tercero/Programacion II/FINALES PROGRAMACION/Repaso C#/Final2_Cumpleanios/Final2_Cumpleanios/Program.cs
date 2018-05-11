using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Cumpleanios
{
    class Program
    {
        public static void Felicitar(object sender, CumplirAniosEventArgs e)
        {
            Console.WriteLine("Feliz cumpleaños, {0}! Ahora tenés {1} años :)", e.nombre, e.edad);
        }
        static void Main(string[] args)
        {
            Persona Persona = new Persona("Alejandro", "Barsotti", 20);
            Persona.MostrarEdad();
            Persona.CumplioAnios += new EventHandler<CumplirAniosEventArgs>(Felicitar);
            Persona.Cumplir_Anios();
            Persona.MostrarEdad();

            Console.ReadLine();

        }

    }
}
