using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Figuras
{
    class Program
    {
        static void Main(string[] args)
        {
            Rectangulo Rectangulo = new Rectangulo(10,5);
            Rectangulo.Inicio_Calculo += new EventHandler<FigurasEventArgs>(IniciodelCalculo);
            Rectangulo.Fin_Calculo += new EventHandler<FigurasEventArgs>(FindelCalculo);
            Cuadrado Cuadrado = new Cuadrado(5,2);
            Cuadrado.Inicio_Calculo += new EventHandler<FigurasEventArgs>(IniciodelCalculo);
            Cuadrado.Fin_Calculo += new EventHandler<FigurasEventArgs>(FindelCalculo);
            Triangulo Triangulo = new Triangulo(3, 4);
            Triangulo.AgregarEvento(IniciodelCalculo, FindelCalculo);  //Para hacerlo distinto, probando
            Rectangulo.Calcular_Area();
            Cuadrado.Calcular_Area();
            Triangulo.Calcular_Area();

            Console.ReadLine();
        }
        public static void IniciodelCalculo(object sender, FigurasEventArgs e)
        {
	        Console.WriteLine("Iniciado el cálculo del área del {0}. Su valor actual es {1}.",e.nombre,e.area);
        }
        public static void FindelCalculo(object sender, FigurasEventArgs e)
        {
            Console.WriteLine("Finalizado el cálculo del área del {0}. Su nuevo valor es {1}.", e.nombre, e.area);
        }
    }
}
