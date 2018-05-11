using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Figuras
{
    class Triangulo : Figura
    {
        public Triangulo (decimal basep, decimal alturap)
        {
            this._base = basep;
            this.altura = alturap;
        }
        public override decimal Calcular_Area()
        {
            this.OnInicioCalculo(new FigurasEventArgs(this.ToString(), area));
            this.area = this._base * this.altura / 2;
            this.OnFinCalculo(new FigurasEventArgs(this.ToString(), area));
            this.Imprimir_Calculo();
            return area;
        }
        public override string ToString()
        {
            return "Triángulo";
        }

        public void AgregarEvento(EventHandler<FigurasEventArgs> eventoinicio, EventHandler<FigurasEventArgs> eventofin)
        {
            this.Inicio_Calculo += new EventHandler<FigurasEventArgs>(eventoinicio);
            this.Fin_Calculo += new EventHandler<FigurasEventArgs>(eventofin);
        }
    }
}
