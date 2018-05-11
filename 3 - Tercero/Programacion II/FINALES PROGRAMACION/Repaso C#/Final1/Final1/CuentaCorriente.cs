using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final1
{
    public class CuentaCorriente : CuentaBancaria
    {
        private decimal limitedescubierto;
        public decimal LimiteDescubierto
        {
            get { return this.limitedescubierto; }
            set
            {
                if (value >= 0)
                    this.limitedescubierto = value;
            }
        }
        public override decimal Extraer(decimal monto)
        {
            if (monto <= (this.Saldo + this.limitedescubierto))
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
