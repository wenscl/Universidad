using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final1
{
    public abstract class CuentaBancaria
    {
        protected decimal saldo;
        public decimal Saldo
        {
            get { return saldo; }
        }
        public void Depositar(decimal monto)
        {
            this.saldo += monto;
        }
        public abstract decimal Extraer(decimal monto);
        public void ImprimirSaldo()
        {
            Console.WriteLine("El saldo de la cuenta es de ${0}.", this.saldo);
        }
    }
}
