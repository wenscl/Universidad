using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public static class ListExtensions
    {
        public static void Mezclar<T>(this IList<T> Cartas)
        {
            Random rng = new Random();
            int n = Cartas.Count;
            while (n > 1)
            {
                n--;
                int k = rng.Next(n + 1);
                T value = Cartas[k];
                Cartas[k] = Cartas[n];
                Cartas[n] = value;
            }
        }
    }
}
