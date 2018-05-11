using System;
using System.Diagnostics;

namespace ChessNotationConverter
{
    class Program
    {
        static void Main(string[] args)
        {
            var respuesta = Methods.HandleRequest();
            Console.WriteLine(respuesta.Message);

            if (Debugger.IsAttached)
            {
                Console.WriteLine("Presione una tecla para salir");
                Console.ReadKey();
            }
        }
    }
}
