using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final1
{
    public class CajaAhorro : CuentaBancaria
    {
        public override decimal Extraer(decimal monto)
        {
            if (this.Saldo >= monto)
            {
                this.saldo -= monto;
                return monto;
            }
            else
            {
                Console.WriteLine("El saldo es insuficiente para esta operación.");
                return 0;
            }
        }
    }
}
