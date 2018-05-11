using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Figuras
{
    public class FigurasEventArgs : EventArgs
    {
        public string nombre { get; set; }
        public decimal area { get; set; }
        public FigurasEventArgs(string nombre, decimal area)
        {
            this.nombre = nombre;
            this.area = area;
        }
    }
}
