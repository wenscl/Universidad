using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Final1
{
    class Program
    {
        static void Main(string[] args)
        {
            CajaAhorro CajaAhorro = new CajaAhorro();
            CajaAhorro.Depositar(1500);
            CajaAhorro.Extraer(500);
            CajaAhorro.ImprimirSaldo();
            CuentaCorriente CuentaCorriente = new CuentaCorriente();
            CuentaCorriente.LimiteDescubierto = 500;
            CuentaCorriente.Extraer(500);
            CuentaCorriente.ImprimirSaldo();
            CuentaCorriente.Depositar(1000);
            CuentaCorriente.ImprimirSaldo();
            CuentaCorriente.Extraer(2000);
            CuentaCorriente.ImprimirSaldo();
            CuentaCorriente.Extraer(1500);
            CuentaCorriente.ImprimirSaldo();

            Console.ReadLine();
        }
    }
}
