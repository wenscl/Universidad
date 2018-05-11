using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Figuras
{
    public class Cuadrado : Figura
    {
        public Cuadrado (decimal basep, decimal alturap)
        {
            this._base = basep;
            this.altura = alturap;
        }
        public override decimal Calcular_Area()
	    {
            this.OnInicioCalculo(new FigurasEventArgs(this.ToString(), area));
	    	this.area = this._base*this.altura;
            this.OnFinCalculo(new FigurasEventArgs(this.ToString(), area));
    		this.Imprimir_Calculo();
	    	return area;
	    }
        public override string ToString()
        {
            return "Cuadrado";
        }
    }
}
