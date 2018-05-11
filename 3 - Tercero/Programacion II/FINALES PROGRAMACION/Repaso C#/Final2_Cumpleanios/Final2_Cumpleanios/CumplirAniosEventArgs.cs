using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final2_Cumpleanios
{
    public class CumplirAniosEventArgs : EventArgs
    {
        public string nombre { get; set; }
        public int edad { get; set; }
        public CumplirAniosEventArgs(string nombree, int edade)
        {
            this.nombre = nombree;
            this.edad = edade;
        }
    }
}
