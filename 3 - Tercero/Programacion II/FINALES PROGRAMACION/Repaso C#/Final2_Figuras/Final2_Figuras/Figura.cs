using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Figuras
{
    public abstract class Figura
    {
        public decimal _base { get; set; }
        public decimal altura { get; set; }
        public decimal area { get; set; }
        public abstract decimal Calcular_Area();
        public virtual void Imprimir_Calculo()
        {
            Console.WriteLine("El área es: {0}.", area);
        }
        public event EventHandler<FigurasEventArgs> Inicio_Calculo;
        public event EventHandler<FigurasEventArgs> Fin_Calculo;

        public virtual void OnInicioCalculo(FigurasEventArgs e)
        {
            if (Inicio_Calculo != null)
                Inicio_Calculo(this, e);
        }
        public virtual void OnFinCalculo(FigurasEventArgs e)
        {
            if (Fin_Calculo != null)
                Fin_Calculo(this, e);
        }
    }
}
